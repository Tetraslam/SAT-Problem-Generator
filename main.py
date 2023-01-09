import random

# Generate a random SAT problem with a given number of variables and clauses
def generate_sat_problem(num_vars, num_clauses):
    # Generate a random list of variables
    variables = [random.randint(0, 1) for _ in range(num_vars)]

    # Generate a list of random clauses
    clauses = []
    for _ in range(num_clauses):
        # Choose a random variable
        var = random.randint(0, num_vars - 1)
        # Choose a random negation value (True or False)
        neg = random.choice([True, False])
        clause = (var, neg)
        clauses.append(clause)

    return variables, clauses

# Check whether a SAT problem is satisfiable
def is_satisfiable(variables, clauses):
    # Evaluate each clause
    for clause in clauses:
        var, neg = clause
        value = variables[var]
        # If the clause is not satisfied, the problem is not satisfiable
        if (neg and not value) or (not neg and value):
            return False
    # If all clauses are satisfied, the problem is satisfiable
    return True

# Test the SAT problem generator
num_vars = 10
num_clauses = 5
variables, clauses = generate_sat_problem(num_vars, num_clauses)
print("Variables:", variables)

print("Clauses:", clauses)

# Check whether the SAT problem is satisfiable
result = is_satisfiable(variables, clauses)
print("Satisfiable:", result)