# Software Quality Assurance and Testing Assignment 2
This whole assignment is designed to demonstrate a students ability to develop in a "test first" manner. 

## main menu
this main menu is meant to be operable from a command line environment. Utilizing a simple text check, will execute based upon user input. 

### possible inputs
| input | action |
| ----- | ------ |
| `menu` | view options in program |
| `bmi` | run bmi calculator |
| `retire` | run retirement calculator |
| `end` | end program |

## BMI calculator
this section includes the functions for a BMI calculator using inputs such as 

| variable | description |
| -------- | ----------- |
| `weight`   | weight in pounds |
| `height_f` | height measurable in feet |
| `height_i` | height measurable in inches |

these inputs get converted to metric using the functions `convert_to_meters` and `convert_to_kg` functions. 

Finally using these metric numbers, BMI is calculated by dividing mass (`kg`) by height<sup>2</sup> (`height_m`)

### BMI ranges
| range | category |
| ----- | -------- |
| `bmi < 18.5`   | __underweight__ |
| `18.5 <= bmi < 25` | __normal__ |
| `25 <= bmi < 30` | __overweight__ |
| `bmi >= 30` | __Obese__ |

BMI is then categorized by ranges of numbers shown above. 

