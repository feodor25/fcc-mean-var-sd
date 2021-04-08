# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([24,75,3,56,87,649,2,76,78]))

# Run unit tests automatically
main(module='test_module', exit=False)