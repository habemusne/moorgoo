module BookpricesHelper
  def inverseStatusQuote(status)
    status == 0 ? "Already Sold" : "Sell Again" 
  end

end
