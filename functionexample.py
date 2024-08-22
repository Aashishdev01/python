def bill(price,gst):
  gst_amount = price*gst/100
  total_price = price+gst_amount
  print('-----bill-------')
  print('Price  = ','₹',price)
  print('Gst  = ',gst,'%')
  print('Gst Amount = ','₹',gst_amount)
  print('Total = ','₹',total_price)


bill(1200,18)
bill(6500,9)
bill(8900,12)

#output
----bill-------
Price  =  ₹ 1200
Gst  =  18 %
Gst Amount =  ₹ 216.0
Total =  ₹ 1416.0
-----bill-------
Price  =  ₹ 6500
Gst  =  9 %
Gst Amount =  ₹ 585.0
Total =  ₹ 7085.0
-----bill-------
Price  =  ₹ 8900
Gst  =  12 %
Gst Amount =  ₹ 1068.0
Total =  ₹ 9968.0
