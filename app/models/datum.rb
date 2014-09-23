class Datum < ActiveRecord::Base
  def self.increToLinear(li, base)
    num = base
    result = []
    li.each do |i|
      num += i
      result << num
    end
    result
  end

  def self.formTime(size, interval)
    result = []
    size.times do |i|
      result << (Date.today - (size - 1 - i) * interval).to_s
    end
    result
  end
end
