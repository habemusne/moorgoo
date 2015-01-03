class TutorRequestsController < ApplicationController
  def new
    @request = TutorRequest.new
  end

  def create
    @request = TutorRequest.create(tutor_request_params)
  end

  private
    def tutor_request_params
      params.require(:tutor_request).permit(:school, :course, :length, :area, :time_one, :time_two, :time_three, :user_id, :frequency, :paid)
    end
end
