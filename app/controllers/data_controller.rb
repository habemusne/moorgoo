class DataController < ApplicationController
  def index
    fourMA = threeMA = twoMA = oneMA = zeroMA = 0
    fourWA = threeWA = twoWA = oneWA = zeroWA = 0
    fourDA = threeDA = twoDA = oneDA = zeroDA = 0
    Bookprice.all.each do |b|
      if b.created_at > 1.month.ago
        zeroMA += 1
        if b.created_at > 1.week.ago
          zeroWA += 1
          if b.created_at > 1.day.ago
            zeroDA += 1
          elsif b.created_at > 2.day.ago
            oneDA += 1
          elsif b.created_at > 3.day.ago
            twoDA += 1
          elsif b.created_at > 4.day.ago
            threeDA += 1
          else
            fourDA += 1
          end
        elsif b.created_at > 2.week.ago
          oneWA += 1
        elsif b.created_at > 3.week.ago
          twoWA += 1
        elsif b.created_at > 4.week.ago
          threeWA += 1
        else
          fourWA += 1
        end
      elsif b.created_at > 2.month.ago
        oneMA += 1
      elsif b.created_at > 3.month.ago
        twoMA += 1
      elsif b.created_at > 4.month.ago
        threeMA += 1
      else
        fourMA += 1
      end
    end
    @season_incre = [fourMA, threeMA, twoMA, oneMA, zeroMA]
    @month_incre = [fourWA, threeWA, twoWA, oneWA, zeroWA]
    @week_incre = [fourDA, threeDA, twoDA, oneDA, zeroDA]
    @season_linear = Datum.increToLinear(@season_incre, 0)
    @month_linear = Datum.increToLinear(@month_incre, @season_linear[-2])
    @week_linear = Datum.increToLinear(@week_incre, @month_linear[-2])
  end
end
