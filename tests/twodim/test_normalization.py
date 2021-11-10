

def test_port():
    # Horses with dividends 2.0, 3.0 and 6.0
    from punting.onedim.onenormalization import normalize_probabilities
    X = [ [ 1.0, -1.0, -1.0],
          [ -1.0, 2.0, -1.0],
          [ -1.0, -1.0, 5.0],
          [-1.0, -1.0, 5.5]]
    p = normalize_probabilities( [1/1.9, 1/3, 1/6.0])