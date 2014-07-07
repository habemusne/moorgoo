module ApplicationHelper
  def has_alert?
    not flash[:alert].nil?
  end
end
