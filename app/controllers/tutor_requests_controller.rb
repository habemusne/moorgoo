require 'securerandom'

class TutorRequestsController < ApplicationController
  def new
    @request = TutorRequest.new
  end

  def create
    @request = current_user.tutor_requests.build(tutor_request_params)
    @request.update_attribute(:code, SecureRandom.base64)
    UserMailer.pay(current_user, @request).deliver
  end

  private
    def tutor_request_params
      params.require(:tutor_request).permit(:school, :course, :length, :area, :time_one, :time_two, :time_three, :user_id, :frequency, :paid)
    end
end
