-- Example SQL validation: verify that a transfer created two ledger rows (debit + credit).
-- Replace schema/table names and <TRANSACTION_ID> with real values.

SELECT COUNT(*) AS ledger_rows
FROM ledger_entries
WHERE transaction_id = '<TRANSACTION_ID>';

-- Expect ledger_rows = 2
