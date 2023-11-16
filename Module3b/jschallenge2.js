function lengthConverter(value, fromUnit, toUnit) {
  // Define conversion factors for common length units
  const conversionRate = {
    centimeters: 1,     // 1 cm is 1 cm
    millemeters: 10, // 10- mm is approximately 1 centimeters
    inches: 0.393701 // 1 inch is approximately 0.393701 meters
    // Add more units and conversion factors as needed
  };

  // Check if the units are known, and if so, perform the conversion
  if (conversionRate[fromUnit] && conversionRate[toUnit]) {
    const result = (value * conversionRate[fromUnit]) / conversionRate[toUnit];
    return result;
  } else {
    return "Units not recognized or conversion not supported.";
  }
}

// Example usage:
const lengthInmillemeters = 10;
const  lengthConverters= lengthConverter(lengthInmillemeters, "centimeters", "millemeters");
console.log(+lengthInmillemeters+ " millemeters is approximately " +lengthConverters + " centimeters.");
