class Admins::SessionsController < Devise::SessionsController
  def new
    super
  end

  def create
    super
    Bookprice.find(cookies.signed[:tempPrice]).update_attribute(:user_id, current_user.id) unless cookies.signed[:tempPrice].nil?
  end

  def destroy
    super
  end
end
