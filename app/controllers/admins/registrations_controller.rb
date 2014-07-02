class Admins::RegistrationsController < Devise::RegistrationsController
  def new
    super
    @user = User.new
  end

  def create
    devise_parameter_sanitizer.for(:sign_up) << :name
    super
    Bookprice.find(cookies.signed[:tempPrice]).update_attribute(:user_id, current_user.id) unless cookies.signed[:tempPrice].nil?
  end

  def cancel
    super
  end

  def edit
    super
  end

  def update
    super
  end

  def destroy
    super
  end

end
