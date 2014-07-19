class Admins::SessionsController < Devise::SessionsController
  def new
    super
  end

  def create
    super
    unless cookies.signed[:tempPrice].nil?
      bookprice = Bookprice.find(cookies.signed[:tempPrice])
      bookprice.update_attribute(:user_id, current_user.id)
      flash[:success] = "#{view_context.link_to('VIEW', bookprice.book)}"
      cookies.signed[:tempPrice] = nil
    end
  end

  def destroy
    super
    flash[:notice] = nil
  end
end
