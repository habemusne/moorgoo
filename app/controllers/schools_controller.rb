class SchoolsController < ApplicationController
  def show
    cookies.signed[:perm_school] = { value: @school.id, expires: 20.years.from_now.utc}
  end
end
