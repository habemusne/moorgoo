class TutorsController < ApplicationController
  def new
    @tutor = Tutor.new
  end

  def create
  end
end
