task :randomizy => :environment do
  Bookprice.all.each do |b|
    b.update_attribute(:created_at, Date.today - rand(150))
  end
  Bookprice.last(500).each do |b|
    b.update_attribute(:created_at, Date.today - rand(30))
  end
  Bookprice.last(100).each do |b|
    b.update_attribute(:created_at, Date.today - rand(7))
  end
end