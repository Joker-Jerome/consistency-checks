import consistency_checks

# Will succeed
consistency_checks.assert_equal(
    '1+1 should be 2',
    'SELECT 1+1',
    'SELECT 2'
)

# Will fail
consistency_checks.assert_equal(
    '1+2 equals 2',
    'SELECT 1+2',
    'SELECT 2'
)
