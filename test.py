from db import run_query

print(run_query("SELECT COUNT(*) AS total FROM passengers"))