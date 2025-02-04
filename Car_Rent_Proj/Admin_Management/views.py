from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminUser
from .forms import AdminUserForm  # Assuming you'll create a form for AdminUser

@login_required
def admin_user_list(request):
    """View to list all admin users."""
    admin_users = AdminUser.objects.all()
    return render(request, 'admin_management/admin_user_list.html', {'admin_users': admin_users})

@login_required
def create_admin_user(request):
    """View to create a new admin user."""
    if request.method == "POST":
        form = AdminUserForm(request.POST)
        if form.is_valid():
            admin_user = form.save(commit=False)
            admin_user.user.save()  # Save the associated User first
            admin_user.save()  # Then save the AdminUser
            return redirect('admin_user_list')  # Redirect to the list of admin users
    else:
        form = AdminUserForm()

    return render(request, 'admin_management/create_admin_user.html', {'form': form})

@login_required
def edit_admin_user(request, user_id):
    """View to edit an existing admin user."""
    admin_user = get_object_or_404(AdminUser, user__id=user_id)

    if request.method == "POST":
        form = AdminUserForm(request.POST, instance=admin_user)
        if form.is_valid():
            form.save()
            return redirect('admin_user_list')  # Redirect to the list of admin users
    else:
        form = AdminUserForm(instance=admin_user)

    return render(request, 'admin_management/edit_admin_user.html', {'form': form})
