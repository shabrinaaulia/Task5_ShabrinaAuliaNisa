-- (opsional) hapus data lama biar isi ulang dari awal
TRUNCATE TABLE Q3_Q4_Review;

-- isi ulang data dengan logika promo yang benar
INSERT INTO Q3_Q4_Review (purchase_date, total_price, promo_code, sales_after_promo)
SELECT 
    s.purchase_date,
    (s.quantity * m.price)::NUMERIC AS total_price,
    p.promo_name AS promo_code,
    -- kalau price_deduction NULL, maka total price-nya tetap (tidak dikurangi promo)
    (s.quantity * m.price - COALESCE(p.price_deduction, 0))::NUMERIC AS sales_after_promo
FROM 
    sales_table s
JOIN 
    marketplace_table m ON s.item_id = m.item_id
LEFT JOIN 
    promo_code p ON s.promo_id = p.promo_id
WHERE 
    s.purchase_date BETWEEN '2022-07-01' AND '2022-12-31';
SELECT * FROM Q3_Q4_Review;
