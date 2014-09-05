class Admins::SessionsController < Devise::SessionsController
  def new
    super
  end

  def create
    check_confirmability
    super
    unless cookies.signed[:tempPrice].nil?
      bookprice = Bookprice.find(cookies.signed[:tempPrice])
      bookprice.update_attribute(:user_id, current_user.id)
      flash[:success] = "Your offer is saved! #{view_context.link_to('VIEW', school_book_path(@school.name, bookprice.book))}"
      cookies.signed[:tempPrice] = nil
    end
  end

  def destroy
    super
    flash[:notice] = nil
  end

  private

  def check_confirmability
    user = User.where(:email=>params[:user][:email])
    unless user.empty?
      flash[:notice] = "Please verify your account first!" if not user.first.confirmed?
    end
  end


  protected

  def after_sign_in_path_for(resource)
    params[:redirect] || '/schools/ucsd'
  end
end
