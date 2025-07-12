export const decodedValue = (bands) => COLORS.findIndex(color=>color===bands[0])*10 + COLORS.findIndex(color=>color===bands[1])
export const COLORS = ['black','brown','red','orange','yellow','green','blue','violet','grey','white'];
