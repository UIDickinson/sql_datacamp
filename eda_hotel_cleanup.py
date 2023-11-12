df = pd.read_csv("hotel_bookings_clean.csv")

def aggregate_deposit_types(row):
   if row['deposit_type_No_Deposit'] == True:
      return 'no deposit made'
   if row['deposit_type_Non_Refund'] == True:
      return 'full deposit made'
   if row['deposit_type_Refundable'] == True:
      return 'partial deposit made'
df['deposit_type'] = df.apply(aggregate_deposit_types, axis=1)

df.to_csv("hotel_bookings_clean_v2.csv", index=False)