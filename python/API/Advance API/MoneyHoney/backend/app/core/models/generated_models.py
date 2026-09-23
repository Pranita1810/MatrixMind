from sqlalchemy import BigInteger, Column, Float, Identity, Integer, MetaData, String, Table



metadata = MetaData()





t_ABB_minute = Table(

    'ABB_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ADANIENSOL_minute = Table(

    'ADANIENSOL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ADANIENT_minute = Table(

    'ADANIENT_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ADANIGREEN_minute = Table(

    'ADANIGREEN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ADANIPORTS_minute = Table(

    'ADANIPORTS_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ADANIPOWER_minute = Table(

    'ADANIPOWER_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_AMBUJACEM_minute = Table(

    'AMBUJACEM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_APOLLOHOSP_minute = Table(

    'APOLLOHOSP_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ASIANPAINT_minute = Table(

    'ASIANPAINT_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ATGL_minute = Table(

    'ATGL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_AXISBANK_minute = Table(

    'AXISBANK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BAJAJ_AUTO_minute = Table(

    'BAJAJ-AUTO_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BAJAJFINSV_minute = Table(

    'BAJAJFINSV_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BAJAJHFL_minute = Table(

    'BAJAJHFL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BAJAJHLDNG_minute = Table(

    'BAJAJHLDNG_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BAJFINANCE_minute = Table(

    'BAJFINANCE_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BANKBARODA_minute = Table(

    'BANKBARODA_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BEL_minute = Table(

    'BEL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BHARTIARTL_minute = Table(

    'BHARTIARTL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BHEL_minute = Table(

    'BHEL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BOSCHLTD_minute = Table(

    'BOSCHLTD_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BPCL_minute = Table(

    'BPCL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_BRITANNIA_minute = Table(

    'BRITANNIA_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_CANBK_minute = Table(

    'CANBK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_CGPOWER_minute = Table(

    'CGPOWER_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_CHOLAFIN_minute = Table(

    'CHOLAFIN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_CIPLA_minute = Table(

    'CIPLA_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_COALINDIA_minute = Table(

    'COALINDIA_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_CUMMINSIND_minute = Table(

    'CUMMINSIND_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_DABUR_minute = Table(

    'DABUR_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_DIVISLAB_minute = Table(

    'DIVISLAB_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_DLF_minute = Table(

    'DLF_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_DMART_minute = Table(

    'DMART_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_DRREDDY_minute = Table(

    'DRREDDY_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_EICHERMOT_minute = Table(

    'EICHERMOT_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ENRIN_minute = Table(

    'ENRIN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ETERNAL_minute = Table(

    'ETERNAL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_GAIL_minute = Table(

    'GAIL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_GODREJCP_minute = Table(

    'GODREJCP_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_GRASIM_minute = Table(

    'GRASIM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HAL_minute = Table(

    'HAL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HAVELLS_minute = Table(

    'HAVELLS_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HCLTECH_minute = Table(

    'HCLTECH_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HDFCAMC_minute = Table(

    'HDFCAMC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HDFCBANK_minute = Table(

    'HDFCBANK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HDFCLIFE_minute = Table(

    'HDFCLIFE_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HEROMOTOCO_minute = Table(

    'HEROMOTOCO_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HINDALCO_minute = Table(

    'HINDALCO_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HINDUNILVR_minute = Table(

    'HINDUNILVR_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HINDZINC_minute = Table(

    'HINDZINC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_HYUNDAI_minute = Table(

    'HYUNDAI_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ICICIBANK_minute = Table(

    'ICICIBANK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ICICIGI_minute = Table(

    'ICICIGI_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ICICIPRULI_minute = Table(

    'ICICIPRULI_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_INDHOTEL_minute = Table(

    'INDHOTEL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_INDIGO_minute = Table(

    'INDIGO_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_INDUSINDBK_minute = Table(

    'INDUSINDBK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_INFY_minute = Table(

    'INFY_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_IOC_minute = Table(

    'IOC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_IRCTC_minute = Table(

    'IRCTC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_IRFC_minute = Table(

    'IRFC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ITC_minute = Table(

    'ITC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_JINDALSTEL_minute = Table(

    'JINDALSTEL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_JIOFIN_minute = Table(

    'JIOFIN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_JSWENERGY_minute = Table(

    'JSWENERGY_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_JSWSTEEL_minute = Table(

    'JSWSTEEL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_KOTAKBANK_minute = Table(

    'KOTAKBANK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_LICI_minute = Table(

    'LICI_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_LODHA_minute = Table(

    'LODHA_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_LTM_minute = Table(

    'LTM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_LT_minute = Table(

    'LT_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MARUTI_minute = Table(

    'MARUTI_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MAXHEALTH_minute = Table(

    'MAXHEALTH_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MAZDOCK_minute = Table(

    'MAZDOCK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MM_minute = Table(

    'MM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MM_minute_new = Table(

    'MM_minute_new', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MOTHERSON_minute = Table(

    'MOTHERSON_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_MUTHOOTFIN_minute = Table(

    'MUTHOOTFIN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_NAUKRI_minute = Table(

    'NAUKRI_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_NESTLEIND_minute = Table(

    'NESTLEIND_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_NHPC_minute = Table(

    'NHPC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_NIFTY_50_minute = Table(

    'NIFTY 50_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_NIFTY_BANK_minute = Table(

    'NIFTY BANK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_NTPC_minute = Table(

    'NTPC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ONGC_minute = Table(

    'ONGC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_PFC_minute = Table(

    'PFC_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_PIDILITIND_minute = Table(

    'PIDILITIND_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_PNB_minute = Table(

    'PNB_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_POWERGRID_minute = Table(

    'POWERGRID_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_RECLTD_minute = Table(

    'RECLTD_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_RELIANCE_minute = Table(

    'RELIANCE_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SBILIFE_minute = Table(

    'SBILIFE_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SBIN_minute = Table(

    'SBIN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SHREECEM_minute = Table(

    'SHREECEM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SHRIRAMFIN_minute = Table(

    'SHRIRAMFIN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SIEMENS_minute = Table(

    'SIEMENS_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SOLARINDS_minute = Table(

    'SOLARINDS_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_SUNPHARMA_minute = Table(

    'SUNPHARMA_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TATACAP_minute = Table(

    'TATACAP_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TATACONSUM_minute = Table(

    'TATACONSUM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TATAPOWER_minute = Table(

    'TATAPOWER_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TATASTEEL_minute = Table(

    'TATASTEEL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TCS_minute = Table(

    'TCS_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TECHM_minute = Table(

    'TECHM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TITAN_minute = Table(

    'TITAN_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TMCV_minute = Table(

    'TMCV_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TMPV_minute = Table(

    'TMPV_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TORNTPHARM_minute = Table(

    'TORNTPHARM_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TRENT_minute = Table(

    'TRENT_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_TVSMOTOR_minute = Table(

    'TVSMOTOR_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ULTRACEMCO_minute = Table(

    'ULTRACEMCO_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_UNIONBANK_minute = Table(

    'UNIONBANK_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_UNITDSPR_minute = Table(

    'UNITDSPR_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_VBL_minute = Table(

    'VBL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_VEDL_minute = Table(

    'VEDL_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_WIPRO_minute = Table(

    'WIPRO_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)





t_ZYDUSLIFE_minute = Table(

    'ZYDUSLIFE_minute', metadata,

    Column('date', String(collation='SQL_Latin1_General_CP1_CI_AS')),

    Column('open', Float(53)),

    Column('high', Float(53)),

    Column('low', Float(53)),

    Column('close', Float(53)),

    Column('volume', BigInteger),

    Column('id', Integer, Identity(start=1, increment=1), nullable=False)

)

