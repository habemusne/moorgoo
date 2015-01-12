class UserMailer < ActionMailer::Base
  default from: "coolmich00@gmail.com"

  def pay(user, request)
    @user = user
    @request = request
    @url = "https://www.payzo.io/moorgoo"
    mail(to: [user.email, "moorgoo2014@gmail.com"], subject: 'Thank you for your request of tutoring')
  end
end
