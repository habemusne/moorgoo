require 'open-uri'

task :parser => :environment do
  f = File.open(ARGV[1])
  admin_id = User.where(:email=>'z2tao@ucsd.edu').first.id
  school_id = School.where(:name=>'ucsd').first.id

  f.each do |line|
  # line = "Physics for scientists and engineers vol 1 + solution manual:partner_lowest_price:$9.97,Sellers:[Shanna:4157638632|None|9780558564926|Phys 2A|None|Like New|August 10, 2014|$30|8&nbsp;total,ihaiderx:9255777557|None|9780558564926|Phys 2A|None|Used|April 14, 2014|$40|18&nbsp;total,chiaming0302:4088884575|None|9780558564926|None|None|Like New|May 30, 2014|$35|8&nbsp;total,];"
    title, restFromTitle = line.split ":partner_lowest_price"
    restFromSeller, sellers = restFromTitle.split "Sellers:["
    firstTimeBook = true
    sellers.split("total,").each do |seller|
      p "iteration"
      if seller.size > 10
        info = seller.split "|"
        isbn = info[2]
        course = info[3].delete(' ').downcase()
        condition = info[5]
        contact = info[0].split(":")[1]
        price = info[7].gsub("$","")
        if firstTimeBook
          @book = Book.create_new_book(isbn, course, title, school_id)
          p "book is inserted with title #{@book.title}"
          firstTimeBook = false
        end
        @book.bookprices.create(:price=>price.to_f, :user_id=>admin_id, :condition=>condition, 
          :contact=>contact)
        p "bookprice inserted"
      end
    end
    firstTimeBook = true
  end
end