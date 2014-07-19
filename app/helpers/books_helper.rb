module BooksHelper
  def odd_arr(n)
    (1..n).step(2).to_a
  end

  def even_arr(n)
    (0..n).step(2).to_a
  end
end
