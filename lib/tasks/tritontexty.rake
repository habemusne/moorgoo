task :tritontexty=>:environment do
  f = File.open(ARGV[1])
  admin_id = User.where(:email=>'sil024@ucsd.edu').first.id
  school_id = School.where(:name=>'ucsd').first.id

  f.each do |line|
    info = line.split "|"
    title = info[0]
    isbn = info[1].to_i.to_s
    author = info[2]
    course = info[3]
    price = info[4].gsub("$","").to_f
    condition = info[5]
    contact = info[6]
    firstTimeBook = true
    if firstTimeBook
      @book = Book.create_new_book(isbn, course, title, school_id, nil)
      p "book is inserted with title #{@book.title}"
      firstTimeBook = false
    end
    @book.bookprices.create(:price=>price, :user_id=>admin_id, :condition=>condition, 
      :contact=>contact)
    p "bookprice inserted"
  end
end