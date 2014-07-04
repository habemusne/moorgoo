module BookpricesHelper
  def inverseStatusQuote(status)
    status == 0 ? "Sold" : "Unsold" 
  end

end
