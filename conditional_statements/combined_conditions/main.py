# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Step 1: Combine the conditions using or
movingProduct = discounted or lowStock

# Step 2: Use not to invert movingProduct for promotion eligibility
promotion = not movingProduct

# Step 3: Print the eligibility status
print("Is the item eligible for promotion?", promotion)