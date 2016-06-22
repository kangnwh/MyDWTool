drop table if exists stock.stock_hist;
CREATE TABLE stock.stock_hist (
  `seq_in_code` bigint(20) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `open` decimal(5,2) DEFAULT NULL,
  `high` decimal(5,2) DEFAULT NULL,
  `close` decimal(5,2) DEFAULT NULL,
  `low` decimal(5,2) DEFAULT NULL,
  `volume` decimal(16,2) DEFAULT NULL,
  `price_change` decimal(5,2) DEFAULT NULL,
  `p_change` decimal(5,2) DEFAULT NULL,
  `ma5` decimal(5,2) DEFAULT NULL,
  `ma10` decimal(5,2) DEFAULT NULL,
  `ma20` decimal(5,2) DEFAULT NULL,
  `v_ma5` decimal(16,2) DEFAULT NULL,
  `v_ma10` decimal(16,2) DEFAULT NULL,
  `v_ma20` decimal(16,2) DEFAULT NULL,
  `turnover` decimal(5,2) DEFAULT NULL,
  `date` date DEFAULT NULL,
  KEY `seq_in_code` (`seq_in_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--drop table stock.stock_agg_by_month;
CREATE TABLE stock.stock_agg_by_month (
        code char(6),
        year smallint,
        month smallint,
        price_change decimal(5,2),
        p_change decimal(5,2),
        volume_avg decimal(15,2)
);

--drop table stock.month_analy;
CREATE TABLE stock.month_analy (
        code char(6),
        month smallint,
        p_change_avg decimal(5,2),
        percent decimal(15,2)
);

-- company basic
drop table if exists stock.comp_basic;
CREATE TABLE stock.comp_basic (
  `code` char(6) DEFAULT NULL,
  `name` nvarchar(6) DEFAULT NULL,
  `industry` nvarchar(4) DEFAULT NULL,
  `area` nvarchar(4) DEFAULT NULL,
  `pe` decimal(16,2) DEFAULT NULL,
  `outstanding` decimal(16,2) DEFAULT NULL,
  `totals` decimal(16,2) DEFAULT NULL,
  `totalAssets` decimal(16,2) DEFAULT NULL,
  `liquidAssets` decimal(16,2) DEFAULT NULL,
  `fixedAssets` decimal(16,2) DEFAULT NULL,
  `reserved` decimal(16,2) DEFAULT NULL,
  `reservedPerShare` decimal(16,2) DEFAULT NULL,
  `esp` decimal(16,2) DEFAULT NULL,
  `bvps` decimal(16,2) DEFAULT NULL,
  `pb` decimal(16,2) DEFAULT NULL,
  `timeToMarket` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;