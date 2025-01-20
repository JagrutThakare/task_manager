from django.utils.timezone import now
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import pytz
from reportlab.pdfgen import canvas
from io import BytesIO
from celery import shared_task
from datetime import timedelta
from tasks.models import Task, Report
from task_manager import settings

@shared_task
def activate_task(task_id):
    print("Task Started")
    try:
        print("Task Executing")
        task = Task.objects.get(id=task_id)
        task.status = 'Pending'
        task.save()
    except Task.DoesNotExist:
        print(f"Task with ID {task_id} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("Task Ended")

@shared_task
def generate_weekly_reports():
    
    kolkata_tz = pytz.timezone('Asia/Kolkata')
    
    now_time = now().astimezone(kolkata_tz)
    end_of_week = now_time.replace(hour=9, minute=0, second=0, microsecond=0) - timedelta(days=now_time.weekday())
    start_of_week = end_of_week - timedelta(days=7)

    print(f"Generating weekly reports for the week {start_of_week} to {end_of_week}")
    users = User.objects.all()

    for user in users:
        if not user.email:
            print(f"User {user.username} has no email address. Skipping.")
            continue

        existing_report = Report.objects.filter(user=user, start_of_week=start_of_week, end_of_week=end_of_week).first()
        if existing_report:
            print(f"Weekly report already sent to {user.username} for previous week.")
            continue

        scheduled_tasks = Task.objects.filter(user=user, updated_at__gte=start_of_week, updated_at__lt=end_of_week, status='Scheduled')
        
        pending_tasks = Task.objects.filter(user=user, status='Pending')
        completed_tasks = Task.objects.filter(user=user, due_date__gte=start_of_week, due_date__lt=end_of_week)

        sections = [
            ("Scheduled Tasks", scheduled_tasks),
            ("Pending Tasks", pending_tasks),
            ("Completed Tasks", completed_tasks),
        ]

        # Buffer for holding the entire report as a single PDF
        buffer = BytesIO()

        p = canvas.Canvas(buffer)
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, 800, f"Weekly Report for {user.username}")
        p.setFont("Helvetica", 12)

        # Set initial y-position
        y_position = 750

        for title, tasks in sections:
            if not tasks.exists():
                continue

            p.drawString(50, y_position, title)
            y_position -= 20

            # Iterate through tasks and add them to the report
            for task in tasks:
                if y_position < 50:
                    p.showPage()  # Start a new page if needed
                    p.setFont("Helvetica", 12)
                    y_position = 750  # Reset y position

                if task.status == 'Scheduled':
                    p.drawString(70, y_position, f"- {task.title} | Scheduled: {task.updated_at.astimezone(kolkata_tz)}")
                else :
                    p.drawString(70, y_position, f"- {task.title} | Created : {task.created_at.astimezone(kolkata_tz)} | Due : {task.due_date.astimezone(kolkata_tz)}")
                
                y_position -= 15

        p.save()
        buffer.seek(0)

        # Send email with the generated PDF
        email = EmailMessage(
            subject=f"Weekly Report for {user.username}",
            body="Please find your weekly task report attached.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        email.attach(f"Weekly_Report_{user.username}.pdf", buffer.getvalue(), "application/pdf")

        try:
            email.send()
            print(f"Email sent to {user.email}")
            Report.objects.create(user=user, start_of_week=start_of_week, end_of_week=end_of_week, is_sent=True)
        except Exception as e:
            print(f"Failed to send email to {user.email}: {e}")

        buffer.close()


