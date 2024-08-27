from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from .models import Chat

def get_gemini_response(user_input):
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ]
    }
    API_KEY = "AIzaSyDYV07h0LgECOegICJNNKUInxGJF00EaHg"
    GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

    params = {'key': API_KEY}
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except requests.exceptions.RequestException as e:
        return {'error': str(e), 'details': e.response.text if e.response else 'No response text'}

@login_required(login_url='login')
def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            answer = get_gemini_response(question)
            # Save the chat in the database
            chat = Chat.objects.create(user=request.user, question=question, answer=answer)
            
            # Ensure that only the 10 latest chats are kept
            total_chats = Chat.objects.filter(user=request.user).count()
            if total_chats > 10:
                excess_chats = Chat.objects.filter(user=request.user).order_by('-created_at')[10:]
                for chat in excess_chats:
                    chat.delete()


    # Fetch the 10 latest chats for the current user
    chats = Chat.objects.filter(user=request.user).order_by('-created_at')[:10]
    return render(request, 'chatbot.html', {'chats': chats})