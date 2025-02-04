from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm  # Assuming you'll create a form for UserProfile

@login_required
def profile_view(request):
    """View to display the user's profile."""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'user_management/profile.html', {'profile': user_profile})

@login_required
def edit_profile(request):
    """View to edit the user's profile."""
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to the profile view after saving
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_management/edit_profile.html', {'form': form})

@login_required
def create_user_profile(request):
    """View to create a new user profile."""
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate the profile with the logged-in user
            user_profile.save()
            return redirect('profile_view')  # Redirect to the profile view after saving
    else:
        form = UserProfileForm()

    return render(request, 'user_management/create_profile.html', {'form': form})
