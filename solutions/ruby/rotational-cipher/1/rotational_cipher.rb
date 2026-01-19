class RotationalCipher
  def self.rotate (text, shift)
    text.split('').map do |c| 
      if c =~ /[A-Z]/ 
         (((c.ord + shift) - ?A.ord) % 26 + ?A.ord).chr
      elsif c =~ /[a-z]/
        (((c.ord + shift) - ?a.ord) % 26 + ?a.ord).chr
      else
        c
      end
    end.join
  end
end