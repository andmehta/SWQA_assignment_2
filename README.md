# SWQA_assignment_2
This whole assignment is designed to demonstrate a students ability to develop in a "test first" manner. 

## BMI calculator
this section includes the functions for a BMI calculator using inputs such as 

| variable | description |
| -------- | ----------- |
| `weight`   | weight in pounds |
| `height_f` | height measurable in feet |
| `height_i` | height measurable in inches |

these inputs get converted to metric using the functions `convert_to_meters` and `convert_to_kg` functions. 

Finally using these metric numbers, BMI is calculated by dividing mass (`kg`) by height<sup>2</sup> (`height_m`)

BMI is then categorized by ranges of numbers

| range | category |
| ----- | -------- |
| BMI < 18.5   | __underweight__ |
| 18.5 <= BMI < 25 | __normal__ |
| 25 <= BMI < 30 | __overweight__ |
| BMI >= 30 | __Obese__ |
