def arithmetic_arranger(problems, output=False):
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  # components of adjusted problem
  overall_top_line = []
  overall_bottom_line = []
  overall_dashes = []
  overall_result_line = []

  ## DETERMINING ERRORS

  # determining if there are too many problems in input
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    # determining if there are any operators other than + or -
    if "+" not in problem and "-" not in problem:
      return "Error: Operator must be '+' or '-'."

    # determining if there are any non-digits in input
    for char in problem:
      if char.isalpha():
        return "Error: Numbers must only contain digits."

    # separating problem into components
    left_operand = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    right_operand = problem.split(" ")[2]

    # determining if there are any numbers with more than four digits
    if len(left_operand) > 4 or len(right_operand) > 4:
      return "Error: Numbers cannot be more than four digits."

    ## FORMATTING

    # determine which operand is longer
    longest = max(len(left_operand), len(right_operand))

    # creating appropriate number of dashes
    num_of_dashes = longest + 2
    dashes = "-" * num_of_dashes

    # right justifying
    top_line = left_operand.rjust(num_of_dashes)
    bottom_line = operator + right_operand.rjust(num_of_dashes - 1)
    answer = str(eval(problem))
    result_line = answer.rjust(num_of_dashes)

    # appending to lists
    overall_top_line += [top_line]
    overall_bottom_line += [bottom_line]
    overall_dashes += [dashes]
    overall_result_line += [result_line]

  # adding spaces between problems
  overall_top_line = "    ".join(overall_top_line)
  overall_bottom_line = "    ".join(overall_bottom_line)
  overall_dashes = "    ".join(overall_dashes)
  overall_result_line = "    ".join(overall_result_line)

  if output == False:
    arranged_problems = f"{overall_top_line}\n{overall_bottom_line}\n{overall_dashes}"
  else:
    arranged_problems = f"{overall_top_line}\n{overall_bottom_line}\n{overall_dashes}\n{overall_result_line}"

  return arranged_problems
