# with return type and arg.
def bill0(price,gst):
  gst_amount = price*gst/100
  total_price = price+gst_amount
  return total_price;
print('Total = ','₹',bill0(1200,18)-10)


#output
Total =  ₹ 1406.0
