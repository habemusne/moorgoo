class BooksController < ApplicationController
  def index
    @books = Book.similar_search(params[:search])
    if @books.empty?
      flash[:alert] = 'No books found'
      redirect_to root_path
    end
    if @books.count == 1
      redirect_to book_path(@books.first)
    end
    # @left = []
    # @right = []
    # books.each do |b|
    #   if b.id % 6 < 3
    #     @left << b
    #   else
    #     @right << b
    #   end
    # end
  end

  def show
    @book ||= Book.find(params[:id])
  end


end
