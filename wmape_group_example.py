def wmape(actual, forecast):
    # we take two series and calculate an output a wmape from it, not to be used in a grouping function

    # make a series called mape
    se_mape = abs(actual-forecast)/actual

    # get a float of the sum of the actual
    ft_actual_sum = actual.sum()

    # get a series of the multiple of the actual & the mape
    se_actual_prod_mape = actual * se_mape

    # summate the prod of the actual and the mape
    ft_actual_prod_mape_sum = se_actual_prod_mape.sum()

    # float: wmape of forecast
    ft_wmape_forecast = ft_actual_prod_mape_sum / ft_actual_sum

    # return a float
    return ft_wmape_forecast

def wmape_gr(df_in, st_actual, st_forecast):
    # we take two series and calculate an output a wmape from it, to be used in a grouping function

    # make a series called mape
    se_mape = abs(df_in[st_actual] - df_in[st_forecast]) / df_in[st_actual]

    # get a float of the sum of the actual
    ft_actual_sum = df_in[st_actual].sum()

    # get a series of the multiple of the actual & the mape
    se_actual_prod_mape = df_in[st_actual] * se_mape

    # summate the prod of the actual and the mape
    ft_actual_prod_mape_sum = se_actual_prod_mape.sum()

    # float: wmape of forecast
    ft_wmape_forecast = ft_actual_prod_mape_sum / ft_actual_sum

    # return a float
    return ft_wmape_forecast

# read in data directly from Dropbox
df = pd.read_csv('https://www.dropbox.com/s/tidf9lj80a1dtd8/data_small_2.csv?dl=1',sep=",",header=0)

# grouping with input columns. wmape_gr uses the Actual column, and Forecast_1 as inputs
df_gr = df.groupby(['City','Person','DT']).apply(wmape_gr,'Actual','Forecast_1')

# for ways on how to do this more easily if you have multiple forecasts, or super-fast with multiple forecasts, see:
# https://stackoverflow.com/questions/54831335/pandas-custom-wmape-function-aggregation-function-to-multiple-columns-without-f
