import numpy as np
import math

def bereken_cumulatief_percentage(score, x, f):
    x = np.array(x)
    f = np.array(f)

    total_frequency = np.sum(f)  # Totale frequentie

    if isinstance(score, (int, float)):
        cumulative_frequencies = np.cumsum(f)
        cumulative_percentages = (cumulative_frequencies / total_frequency) * 100
        return np.round(cumulative_percentages, 1)
    elif isinstance(score, (list, np.ndarray)):
        cumulative_percentages = []
        cumulative_frequency = 0
        for s in score:
            cumulative_frequency += np.sum(f[x <= s])
            cumulative_percentage = (cumulative_frequency / total_frequency) * 100
            cumulative_percentages.append(cumulative_percentage)
        return np.round(cumulative_percentages, 1)
    else:
        return None


def bereken_relatieve_frequenties(frequenties, waarde=None):
    total_observations = np.sum(frequenties)  # Totale aantal observaties

    if waarde is None:
        relative_frequencies = frequenties / total_observations
        return (relative_frequencies * 100).round(2)
    else:
        index = np.where(frequenties == waarde)[0]  # Zoek index van de waarde in de frequenties

        if len(index) > 0:
            frequency = frequenties[index][0]
            relative_frequency = frequency / total_observations
            return (relative_frequency * 100).round(2)
        else:
            return 0.0  # Als de waarde niet in de frequenties voorkomt, retourneer 0.0 als relatieve frequentie


def median_categorical(data):
    data_no_na = data.dropna()
    n = len(data_no_na)
    middle = math.floor(n / 2)
    return data_no_na.sort_values().reset_index(drop=True)[middle]

def outlier_boundaries(x, factor=1.5):
    Q1 = x.quantile(0.25)
    Q3 = x.quantile(0.75)
    I = Q3 - Q1
    return [Q1 - factor * I, Q3 + factor * I]