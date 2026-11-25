import duckdb

bronzejames = duckdb.sql("""

    SELECT DISTINCT 
        session_id,
        customer_id,
        store_id,
        session_date,

    SPLIT_PART(browser_os, ' ', 1) AS browser_name,
    SPLIT_PART(browser_os, ' ', 2) AS os_name,

    TRIM(device_type) AS devices,
    
    COALESCE(session_pages_visited, '0') AS pages_visited,

    CONCAT(browser_os, ' ', device_type) AS devices
    FROM 'bronzejames.parquet'a
""")

bronzejames.write_parquet('silverjames.parquet')