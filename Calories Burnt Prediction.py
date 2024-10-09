{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c3ab7a16-b135-43e7-b403-bf9cd07cefa4",
   "metadata": {},
   "source": [
    "Importing the Dependencies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "ff794e2d-c62d-425a-a090-5e4072c49381",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from xgboost import XGBRegressor\n",
    "from sklearn import metrics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ea3a25f-a204-45d6-9ad6-37ace6369645",
   "metadata": {},
   "source": [
    "Data Collection & Processing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "57cabd79-c6c2-48bf-9625-5becbd5d6d50",
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the data from csv file to a Pandas DataFrame\n",
    "calories = pd.read_csv('calories.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "897df96f-5931-4641-92cd-e4732a9efa88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>User_ID</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>14733363</td>\n",
       "      <td>231.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14861698</td>\n",
       "      <td>66.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11179863</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16180408</td>\n",
       "      <td>71.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>17771927</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    User_ID  Calories\n",
       "0  14733363     231.0\n",
       "1  14861698      66.0\n",
       "2  11179863      26.0\n",
       "3  16180408      71.0\n",
       "4  17771927      35.0"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# print the first 5 rows of the dataframe\n",
    "calories.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "af5ded14-d75e-4a0e-9414-dcf5d62e215c",
   "metadata": {},
   "outputs": [],
   "source": [
    "exercise_data = pd.read_csv('exercise.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "d185bfa1-6d14-4d93-aee7-494abcb26e30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>User_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Heart_Rate</th>\n",
       "      <th>Body_Temp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>14733363</td>\n",
       "      <td>male</td>\n",
       "      <td>68</td>\n",
       "      <td>190.0</td>\n",
       "      <td>94.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>105.0</td>\n",
       "      <td>40.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14861698</td>\n",
       "      <td>female</td>\n",
       "      <td>20</td>\n",
       "      <td>166.0</td>\n",
       "      <td>60.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>94.0</td>\n",
       "      <td>40.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11179863</td>\n",
       "      <td>male</td>\n",
       "      <td>69</td>\n",
       "      <td>179.0</td>\n",
       "      <td>79.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>38.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16180408</td>\n",
       "      <td>female</td>\n",
       "      <td>34</td>\n",
       "      <td>179.0</td>\n",
       "      <td>71.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>40.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>17771927</td>\n",
       "      <td>female</td>\n",
       "      <td>27</td>\n",
       "      <td>154.0</td>\n",
       "      <td>58.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>81.0</td>\n",
       "      <td>39.8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    User_ID  Gender  Age  Height  Weight  Duration  Heart_Rate  Body_Temp\n",
       "0  14733363    male   68   190.0    94.0      29.0       105.0       40.8\n",
       "1  14861698  female   20   166.0    60.0      14.0        94.0       40.3\n",
       "2  11179863    male   69   179.0    79.0       5.0        88.0       38.7\n",
       "3  16180408  female   34   179.0    71.0      13.0       100.0       40.5\n",
       "4  17771927  female   27   154.0    58.0      10.0        81.0       39.8"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "exercise_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb316f28-80d0-4bde-bc81-0f2ce63e49a7",
   "metadata": {},
   "source": [
    "Combining the two Dataframes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "54f8f122-1da9-4f51-8d31-7fe8585e645f",
   "metadata": {},
   "outputs": [],
   "source": [
    "calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "7063692d-210d-4ae1-89ba-769489781876",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>User_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Heart_Rate</th>\n",
       "      <th>Body_Temp</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>14733363</td>\n",
       "      <td>male</td>\n",
       "      <td>68</td>\n",
       "      <td>190.0</td>\n",
       "      <td>94.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>105.0</td>\n",
       "      <td>40.8</td>\n",
       "      <td>231.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14861698</td>\n",
       "      <td>female</td>\n",
       "      <td>20</td>\n",
       "      <td>166.0</td>\n",
       "      <td>60.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>94.0</td>\n",
       "      <td>40.3</td>\n",
       "      <td>66.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11179863</td>\n",
       "      <td>male</td>\n",
       "      <td>69</td>\n",
       "      <td>179.0</td>\n",
       "      <td>79.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>38.7</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16180408</td>\n",
       "      <td>female</td>\n",
       "      <td>34</td>\n",
       "      <td>179.0</td>\n",
       "      <td>71.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>40.5</td>\n",
       "      <td>71.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>17771927</td>\n",
       "      <td>female</td>\n",
       "      <td>27</td>\n",
       "      <td>154.0</td>\n",
       "      <td>58.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>81.0</td>\n",
       "      <td>39.8</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    User_ID  Gender  Age  Height  Weight  Duration  Heart_Rate  Body_Temp  \\\n",
       "0  14733363    male   68   190.0    94.0      29.0       105.0       40.8   \n",
       "1  14861698  female   20   166.0    60.0      14.0        94.0       40.3   \n",
       "2  11179863    male   69   179.0    79.0       5.0        88.0       38.7   \n",
       "3  16180408  female   34   179.0    71.0      13.0       100.0       40.5   \n",
       "4  17771927  female   27   154.0    58.0      10.0        81.0       39.8   \n",
       "\n",
       "   Calories  \n",
       "0     231.0  \n",
       "1      66.0  \n",
       "2      26.0  \n",
       "3      71.0  \n",
       "4      35.0  "
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calories_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "2367e53f-48c6-45b6-80f9-4626e5557e71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(15000, 9)"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking the number of rows and columns\n",
    "calories_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "294d5df2-2547-4887-bd2b-9d3256791fc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 15000 entries, 0 to 14999\n",
      "Data columns (total 9 columns):\n",
      " #   Column      Non-Null Count  Dtype  \n",
      "---  ------      --------------  -----  \n",
      " 0   User_ID     15000 non-null  int64  \n",
      " 1   Gender      15000 non-null  object \n",
      " 2   Age         15000 non-null  int64  \n",
      " 3   Height      15000 non-null  float64\n",
      " 4   Weight      15000 non-null  float64\n",
      " 5   Duration    15000 non-null  float64\n",
      " 6   Heart_Rate  15000 non-null  float64\n",
      " 7   Body_Temp   15000 non-null  float64\n",
      " 8   Calories    15000 non-null  float64\n",
      "dtypes: float64(6), int64(2), object(1)\n",
      "memory usage: 1.0+ MB\n"
     ]
    }
   ],
   "source": [
    "# getting some informations about the data\n",
    "calories_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "c4e17667-9403-4766-8e99-845c85c2a414",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "User_ID       0\n",
       "Gender        0\n",
       "Age           0\n",
       "Height        0\n",
       "Weight        0\n",
       "Duration      0\n",
       "Heart_Rate    0\n",
       "Body_Temp     0\n",
       "Calories      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking for missing values\n",
    "calories_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "878a82f9-ad3a-4822-9732-c720e921e4be",
   "metadata": {},
   "source": [
    "Data Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "c8eba4f6-f01f-4712-8717-ef9128f8a3d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>User_ID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Heart_Rate</th>\n",
       "      <th>Body_Temp</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1.500000e+04</td>\n",
       "      <td>15000.000000</td>\n",
       "      <td>15000.000000</td>\n",
       "      <td>15000.000000</td>\n",
       "      <td>15000.000000</td>\n",
       "      <td>15000.000000</td>\n",
       "      <td>15000.000000</td>\n",
       "      <td>15000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.497736e+07</td>\n",
       "      <td>42.789800</td>\n",
       "      <td>174.465133</td>\n",
       "      <td>74.966867</td>\n",
       "      <td>15.530600</td>\n",
       "      <td>95.518533</td>\n",
       "      <td>40.025453</td>\n",
       "      <td>89.539533</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.872851e+06</td>\n",
       "      <td>16.980264</td>\n",
       "      <td>14.258114</td>\n",
       "      <td>15.035657</td>\n",
       "      <td>8.319203</td>\n",
       "      <td>9.583328</td>\n",
       "      <td>0.779230</td>\n",
       "      <td>62.456978</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000116e+07</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>123.000000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>67.000000</td>\n",
       "      <td>37.100000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.247419e+07</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>164.000000</td>\n",
       "      <td>63.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>88.000000</td>\n",
       "      <td>39.600000</td>\n",
       "      <td>35.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.499728e+07</td>\n",
       "      <td>39.000000</td>\n",
       "      <td>175.000000</td>\n",
       "      <td>74.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>96.000000</td>\n",
       "      <td>40.200000</td>\n",
       "      <td>79.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.744928e+07</td>\n",
       "      <td>56.000000</td>\n",
       "      <td>185.000000</td>\n",
       "      <td>87.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>103.000000</td>\n",
       "      <td>40.600000</td>\n",
       "      <td>138.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.999965e+07</td>\n",
       "      <td>79.000000</td>\n",
       "      <td>222.000000</td>\n",
       "      <td>132.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>41.500000</td>\n",
       "      <td>314.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            User_ID           Age        Height        Weight      Duration  \\\n",
       "count  1.500000e+04  15000.000000  15000.000000  15000.000000  15000.000000   \n",
       "mean   1.497736e+07     42.789800    174.465133     74.966867     15.530600   \n",
       "std    2.872851e+06     16.980264     14.258114     15.035657      8.319203   \n",
       "min    1.000116e+07     20.000000    123.000000     36.000000      1.000000   \n",
       "25%    1.247419e+07     28.000000    164.000000     63.000000      8.000000   \n",
       "50%    1.499728e+07     39.000000    175.000000     74.000000     16.000000   \n",
       "75%    1.744928e+07     56.000000    185.000000     87.000000     23.000000   \n",
       "max    1.999965e+07     79.000000    222.000000    132.000000     30.000000   \n",
       "\n",
       "         Heart_Rate     Body_Temp      Calories  \n",
       "count  15000.000000  15000.000000  15000.000000  \n",
       "mean      95.518533     40.025453     89.539533  \n",
       "std        9.583328      0.779230     62.456978  \n",
       "min       67.000000     37.100000      1.000000  \n",
       "25%       88.000000     39.600000     35.000000  \n",
       "50%       96.000000     40.200000     79.000000  \n",
       "75%      103.000000     40.600000    138.000000  \n",
       "max      128.000000     41.500000    314.000000  "
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# get some statistical measures about the data\n",
    "calories_data.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb8506e2-a659-47c9-ad8c-5b428d476414",
   "metadata": {},
   "source": [
    "Data Visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "0005a556-f917-4200-98ec-e07d58193dc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "451bd7af-9395-4f75-839b-572f48661e2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='count', ylabel='Gender'>"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlMAAAG1CAYAAADdtHHqAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAncUlEQVR4nO3de3TU9Z3/8dckBLkYMInlsrQoiCQCiUkK4S4QkVtBbNGCgOwSbnapkA0rgVZUcBXEgEAqN4EFwSoKLsiCRRStp5ZbxKbKLSRcBAQihMBKIJDM5/eHh/kxJm3CfCaZZOb5OIdz4PudfPN+JypPZ4YvDmOMEQAAADwS5OsBAAAAqjNiCgAAwAIxBQAAYIGYAgAAsEBMAQAAWCCmAAAALBBTAAAAFogpAAAAC8QUAACAhRq+HiBQGGPkdAbezeaDghwBubcUuLsH6t5S4O4eqHtLgbt7oOwdFOSQw+Eo83HEVCVxOBy6dKlARUVOX49SaWrUCFJYWN2A21sK3N0DdW8pcHcP1L2lwN09kPYOD6+r4OCyY4qX+QAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAQAAWCCmAAAALBBTAAAAFogpAAAAC8QUAACABWIKAADAAjEFAABggZgCAACwUMPXAwSS4ODAatcb+wba3lLg7h6oe0uBu3ug7i0F7u6+2NvpNHI6TaV9vlvlMMZU3en8iDFGDofD12MAAFDtFBc7lZ9fUOlBFR5et1zRyDNTlcThcOi1tz7XqdyLvh4FAIBqo0mD+hr/eGcFBTmq7LNTxFQlOpV7UcdOXfD1GAAAwIsC64VeAAAALyOmAAAALBBTAAAAFogpAAAAC8QUAACABWIKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAQAAWCCmAAAALBBTAAAAFogpAAAAC8QUAACABWIKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAQAAWCCmAAAALBBTAAAAFogpAAAAC8QUAACABWIKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQU5ISExOVnp7u6zEAAEA1REwBAABYIKYAAAAsVLuYioyM1Nq1azV06FBFR0erb9++2rt3r9auXavu3bsrPj5eycnJunr1qutj3n33XQ0YMEAxMTGKjY3V0KFD9dVXX/3Dz7F3714NGzZMMTEx6t69u6ZPn67vv/++MtYDAADVTLWLKUl69dVXNXr0aG3cuFGhoaF68skntXXrVi1dulQzZ87URx99pHfffVeStG3bNs2YMUOjR4/WBx98oJUrV6qwsFDPPPNMqdc+ePCgRo4cqa5du+r9999XWlqa9u3bp6SkJBljKnNNAABQDVTLmBo0aJASExPVvHlzDRw4UBcvXtSzzz6rli1bqnfv3rrvvvt0+PBhSdIdd9yhF198UQMHDlSTJk0UGxurRx99VFlZWaVee/ny5ercubOefPJJ3X333Wrbtq3mzJmjzMxM7d69uzLXBAAA1UANXw/gibvuusv189q1a0uSmjZt6jpWq1YtXbt2TZLUrl075eTk6LXXXtORI0d0/PhxHTp0SE6ns9Rr79+/X8ePH1dcXFyJczk5OWrfvr03VwEAANVctYypGjVKjh0UVPqTbJs2bdKUKVM0YMAAxcfHa8iQIcrKytKMGTNKfbzT6dSAAQP05JNPljgXHh5uNzgAAPA71TKmbsXSpUv16KOPavr06a5jH3/8sSTJGCOHw+H2+HvvvVfZ2dluz37l5OTolVdeUUpKikJDQytncAAAUC1Uy/dM3YrGjRtr79692rdvn7755hutXLlSa9askSTXS4E3S0pK0v79+zV9+nTl5OToyy+/1KRJk3Ts2DHdfffdlTw9AACo6vw+pqZNm6Y777xTw4cP12OPPaZPPvlEs2fPlqRSb48QGxurZcuW6cCBA/rlL3+p3/zmN2rWrJlWrlypmjVrVvb4AACginMY/rx/pfnd/C06duqCr8cAAKDauLtJmF6a2E8XLlxWUVHpf3isooSH11VwcNnPO/n9M1MAAAAViZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAAL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w+HQmDFjtHr1aq1Zs0bffPONtm3bpueff161atVye3YMAABAqkLPTEk/vLwWFham+fPnKzc3V40bN9aECRM0evRoj64XEhKi+fPna9asWRowYIDq16+v9u3bKyUlRUuWLNGVK1dKfExSUpJuu+02rV69WrNmzdKdd96pX//615owYYLtegAAwA85zI03K6HC/W7+Fh07dcHXYwAA4BfubhKmlyb204ULl1VU5P37QYaH11VwcNkv4lWZl/kAAACqI2IKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAQAAWCCmAAAALBBTAAAAFogpAAAAC8QUAACABWIKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAQAAWCCmAAAALBBTAAAAFogpAAAAC8QUAACABWIKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwEINXw8QSJo0qO/rEQAA8BtV5fdVhzHG+HqIQGCMkcPh8PUYAAD4leJip/LzC+R0ej9nwsPrKji47BfxeGaqkjgcDl26dEXFxU5fj1JpgoODVK9e7YDbWwrc3QN1bylwdw/UvaXA3b2q7e10mgoJqVtBTFWi4mKniop8/w9eZQvUvaXA3T1Q95YCd/dA3VsK3N0Dde/S8AZ0AAAAC8QUAACABWIKAADAAjEFAABggZgCAACwQEwBAABYIKYAAAAsEFMAAAAWiCkAAAALxBQAAIAFYgoAAMACMQUAAGCBmAIAALBATAEAAFhwGGOMr4cIFMXFTl+PUOmCg4MCcm8pcHcP1L2lwN09UPeWAnf3QNk7KMghh8NR5uOIKQAAAAu8zAcAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAA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o4dZvXq12/nyfB3KukZlW7RokWnZsmWpP1JTU40xxvz5z382/fv3N23atDF9+vQxmzdvdrvG5cuXze9//3vTtm1b07ZtW5OSkmLy8vLcHlPWNXzl0qVL5rnnnjOdO3c2MTExJikpyWRlZbnO++P3vDQ3x5Qx/r33d999Z6ZMmWI6d+5soqOjzeDBg82ePXtc5/159xUrVpjExETTunVr8/DDD5tt27a5zh07dsyMHDnSREdHmy5duph58+aZ4uJit49ftmyZeeCBB0xMTIwZOnSo2b9/v9v58lzDV0aPHm2Sk5NLPefvu3uTwxgf3tAGAACgmuM9UwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAUAVwF1qgOqLmAIAH/v444+Vmprq6zEAeKiGrwcAgEC3cuVKX48AwALPTAEAAFggpgAEJGOMVq5cqb59+yomJkYPPfSQli9f7nrv0ueff66hQ4fq5z//udq3b69Jkybp9OnTro9PT09XZGRkietGRkYqPT1dknTy5ElFRkbqgw8+0IQJExQXF6eEhAQ988wzKigokCQ98cQT2r17t3bv3q3IyEjt2rWrErYH4E28zAcgIM2ePVurVq3SyJEj1blzZ3311VdKS0tTUVGRGjZsqNTUVPXv31/jxo3ThQsXtGDBAg0ePFj/8z//o4iIiFv6XM8995wGDRqkhQsX6u9//7teffVVhYWFadKkSXruuef09NNPux7XokWLilgXQAUipgAEnEuXLumNN97Q8OHDXSHTqVMnfffdd9qzZ48OHjyoLl26aM6cOa6PiY+PV79+/bR8+XJNnjz5lj5ft27dXG8w79ixoz7//HN9+umnmjRpklq0aKHbb79dkhQbG+udBQFUKl7mAxBw/va3v6moqEi9evVyO/7MM89o6tSp+u6779S/f3+3c02bNlVcXJx27959y5/vx5HUqFEj18t8AKo/YgpAwMnPz5ckhYeH/8Nzd955Z4lzd955p/7v//7vlj9f7dq13X4dFBTEfaUAP0JMAQg49erVkyTl5eW5Hf/222916NAhSdK5c+dKfNx3332nsLAwSZLD4ZAkFRcXu85fvny5QuYFULURUwACTkxMjEJCQvTJJ5+4HV+xYoUWLFign/zkJ/rf//1ft3MnTpzQ3/72N8XHx0uS631OZ86ccT3miy++8GieoCD+UwxUZ7wBHUDACQ8P14gRI7Ry5UrVrFlTCQkJyszM1FtvvaXJkycrNDRUU6dO1aRJk/Twww/rwoUL+sMf/qD69etr5MiRkn54U/nMmTP17LPPatSoUTp9+rRee+011a1b95bnqVevnr788kvt2LFDrVq1Uv369b29MoAKREwBCEhPP/20IiIi9Pbbb2vZsmX66U9/qmnTpmnIkCGSpLp162rJkiUaP368br/9dnXt2lUpKSn6yU9+Iklq1qyZXn75ZS1atEhjx47VPffcoxdeeEEvvPDCLc8ybNgwff311xozZoxmzpypAQMGeHVXABXLYXgXJAAAgMd4oR4AAMACMQUAAGCBmAIAALBATAEAAFggpgAAACwQUwAAABaIKQAAAAvEFAAAgAViCgAAwAIxBQAAYIGYAgAAsEBMAQAAWPh/YR/sDzevd08AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plotting the gender column in count plot\n",
    "sns.countplot(calories_data['Gender'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "id": "0c7056f1-86fa-4854-b605-888bdc564b92",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ASUS\\AppData\\Local\\Temp\\ipykernel_17372\\65959470.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(calories_data['Age'])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Age', ylabel='Density'>"
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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pk4M8M4YFINQrconxywF4uvMNrPN/optDqw2e4PsV5aIiIiIejOGJSIiIiI3GJaIiIiI3GBYIiIiInKDYYmIiIjIDYYlIiIiIjcYloiIiIjcYFgiIiIicoNhiYiIiMgNhiUiIiIiNxiWiIiIiNxgWCIiIiJyg2GJiIiIyA2GJSIiIiI3GJaIiIiI3GBYIiIiInKDYYmIiIjIDYYlIiIiIjcYloiIiIjcYFgiIiIicoNhiYiIiMgNhiUiIiIiNxiWiIiIiNxgWCIiIiJyg2GJiIiIyA2GJSIiIiI3GJaIiIiI3GBYIiIiInKDYYmIiIjIDYYlIiIiIjcYloiIiIjcYFgiIiIicoNhiYiIiMgNhiUiIiIiNxiWiIiIiNxgWCIiIiJyg2GJiIiIyA2GJSIiIiI3lHIXQNSdBEHo9DmSJHVDJURE5KsYlshvOQCYzbZOn6fVKKHwfjlEROSjGJbILwmCALPZhtwiA2x2p8fnqZQi0pKjEKpV8QoTEREBYFgiP2ezO2G1OeQug4iIfBgHeBMRERG5wbBERERE5AbDEhEREZEbDEtEREREbjAsEREREbnBsERERETkBsMSERERkRsMS0RERERuMCwRERERucGwREREROQGwxIRERGRGwxLRERERG4wLBERERG5wbBERERE5AbDEhEREZEbDEtEREREbjAsEREREbnBsERERETkBsMSERERkRsMS0RERERuMCwRERERucGwREREROQGwxIRERGRGwxLRERERG4wLBERERG5wbBERERE5IbsYcnpdGLdunWYPHkyRo0ahbvvvhvnzp276PG1tbV4+OGHkZWVhXHjxmHlypUwmUyu/Q6HA+vWrcPUqVMxcuRIzJs3D1999VUPtISIiIj8kexhacOGDdi8eTOeeeYZvPPOO3A6nVi0aBGsVmuHxy9ZsgTFxcV444038PLLL+Prr7/GihUrXPtffvllvP3223jqqafw8ccf49prr8V9992HY8eO9VCLiIiIyJ/IGpasVis2bdqEJUuWYMqUKUhNTcXatWtRXl6OnTt3tjv+4MGDyM7OxgsvvIDhw4djwoQJePrpp/HBBx+goqICAGCz2fDEE09gypQp6NevH+69916EhIRgz549Pd08IiIi8gOyhqWTJ0+iqakJEyZMcG3T6XRIS0vDvn372h2fk5OD2NhYpKSkuLaNGzcO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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# finding the distribution of \"Age\" column\n",
    "sns.distplot(calories_data['Age'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "4a5eea0c-8f9f-4ce8-8440-c6d3b94fe12c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ASUS\\AppData\\Local\\Temp\\ipykernel_17372\\784960979.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(calories_data['Height'])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Height', ylabel='Density'>"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkwAAAG1CAYAAAALEauPAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABqq0lEQVR4nO3deXxV5bn3/8/aU+aZTBAmAZkHgaC0QlGptQ5HRNtqpWKtw6O/pxwnrJ5ajthTh0q1WtTaKsd66tDjo5Va2zpr1cooAgphTkggI5mHPa/fHzvZEhJIyLR2ku/79VovYK21V659s/fOte/7XtdtmKZpIiIiIiLHZbM6ABEREZFIp4RJREREpANKmEREREQ6oIRJREREpANKmEREREQ6oIRJREREpANKmEREREQ6oIRJREREpANKmEREREQ64LA6gIHCNE2Cwcgpmm6zGREVT3+kNuw+tWH3qP26T23YfQO5DW02A8MwOnWuEqYeEgyaVFY2WB0GAA6HjZSUOGprG/H7g1aH0y+pDbtPbdg9ar/uUxt230Bvw9TUOOz2ziVMGpITERER6YASJhEREZEOKGESERER6YASJhEREZEOKGESERER6YASJhEREZEOKGESERER6YASJhEREZEOKGESERER6YASJhEREZEOKGESERER6YASJhEREZEOKGESERER6YDlCVMwGOSxxx5j3rx5zJgxg+uuu47CwsLjnl9VVcVtt91Gbm4uc+bMYeXKlTQ1NbW63tNPP823vvUtZsyYwQUXXMDLL7/c6hpPPvkk48ePb7OJiIiItMdhdQBPPPEEL7zwAg888ABZWVk89NBDXHvttbz++uu4XK425y9btoympiaeffZZamtr+elPf0pjYyMPPvggAE899RRr1qxh5cqVTJkyhU8//ZR77rkHp9PJokWLANi1axcXX3wxy5cv78unKiIWMgzjuMdM0+zDSESkP7K0h8nr9bJmzRqWLVvGggULmDBhAo888gglJSW89dZbbc7fsmULGzZs4MEHH2Ty5MnMnTuXe++9l7Vr11JaWgrAiy++yDXXXMP555/PiBEj+N73vsfFF1/cqpdp9+7dTJo0ifT09FabiAxMAaDe7TvuFrA6QBGJeJb2MOXl5dHQ0MDcuXPD+xITE5k0aRIbN27kwgsvbHX+pk2bSE9PZ8yYMeF9c+bMwTAMNm/e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bNky/H4/d999N263m9zcXJ555plWw1CDVWpqKs8//zz3338/3/nOd3C5XCxcuJA777wzfM53v/td6urq+PWvf011dTVTpkzhv//7v8O30w928+bN46mnnuLxxx/nD3/4AykpKXzzm9/k3//938PnDPbX4JtvvonP5+Ptt9/m7bffbnXskksu4YEHHuCJJ57goYce4g9/+AM5OTk89NBDrUoNDPbPwhO14de//vVwb9HFF1/c5rG7du3CMAxWr17NypUrWbp0KVFRUZx33nncddddfRK/VQzTNE2rgxARERGJZJrDJCIiItIBJUwiIiIiHVDCJCIiItIBJUwiIiIiHVDCJCIiItIBJUwiIiIiHVDCJCJiAVV0EelflDCJyIBw5513cvbZZx/3+Nlnn92qiGZ3r9fVx9TW1nLHHXewadOmk7q2iFhLCZOISDtuuukmVq9e3ePX3blzJ2vXriUYDPb4tUWk92hpFBGRdowYMcLqEEQkgqiHSUQGpZdffpkLLriAKVOmsGDBAn7zm98QCATCx48dXvP5fKxatYr58+czbdo0fvSjH/Haa68xfvx4ioqKWl371Vdf5Vvf+hZTp07l3/7t3/jwww8BWL9+PVdddRUAV111FT/4wQ/64JmKSE9QwiQiA4rf7293O9pTTz3Fz372M+bOnctvf/tbrrzySn7/+9/zs5/97LjXXbFiBX/4wx9YsmQJjz/+OEOGDGn3/OLiYn73u9/x7//+7/zmN7/BMAyWLVvGkSNHmDx5MitWrAhf7z//8z979smLSK/RkJyIDBiHDh1i8uTJJzynrq6OJ554gu9973vhFerPPPNMkpOTufvuu/nhD3/IuHHjWj3m4MGD/PnPf+YnP/kJP/zhDwGYN28eFRUVfPzxx63ODQaDPP7444wZMwaAqKgorr76aj7//HPOOeccxo4dC8DYsWPDfxeRyKeESUQGjPT0dJ588sl2j914440AbNmyBbfbzdlnn92q56ll+O2TTz5pkzCtX78e0zQ577zzWu2/8MIL2yRMKSkp4WQJICcnBwglaiLSfylhEpEBw+VyMXXq1OMeA6iurgbg+uuvb/e8srKyNvsqKysBSEtLa7X/2H8DxMbGtvq3YRgAuitOpJ9TwiQig0piYiIAq1atYtSoUW2ODxkypM2+zMxMACoqKhg6dGh4f0siJSIDnyZ9i8igMn36dJxOJ6WlpUydOjW8ORwOHn744TZ3vAHMmjULu93O22+/3Wr/W2+9ddI/3263dzl2EbGOephEZFBJSUnh2muv5dFHH6W+vp7TTz+d0tJSHn30UQzDYMKECW0eM3z4cC699FIefvhhfD4fEyZM4O233+b9998HwGbr/HfPhIQEAD744AOSkpLa/XkiEnmUMInIoHPzzTeTnp7OCy+8wNNPP01SUhJz587l1ltvDSc0x/rZz35GbGwsa9asob6+nrlz53LjjTfy+OOPt5m3dCLjxo3jwgsv5Pnnn+ejjz7ir3/9a089LRHpRYapFSBFRE6ourqaf/7zn8ybN4+UlJTw/gcffJBXX32V9evXWxidiPQF9TCJiHQgJiaGX/ziF0ycOJGlS5cSGxvL559/zh//+EduuOEGq8MTkT6gHiYRkU7YuXMnv/71r/n8889pampixIgRXH755Vx55ZXh0gEiMnApYRIRERHpgMoKiIiIiHRACZOIiIhIB5QwiYiIiHRACZOIiIhIB5QwiYiIiHRACZOIiIhIB5QwiYiIiHRACZOIiIhIB5QwiYiIiHTg/we3JGGDNQRDFgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# finding the distribution of \"Height\" column\n",
    "sns.distplot(calories_data['Height'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "5b62a2dc-9201-4043-901c-79a9f5e43e5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ASUS\\AppData\\Local\\Temp\\ipykernel_17372\\1532561181.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(calories_data['Weight'])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Weight', ylabel='Density'>"
      ]
     },
     "execution_count": 174,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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oaHL47ua15SUlITf78fn8x33fH6/v0fn6C3DMHA44pugHQ4YlpVYE9FNk27XHjn6A931/u6ef/z9J/Nc7U/s/X3/2n33uRzq+xO5tsGwXz6fafbP/FhbZ+F6PNG+j0Cg4/wYv9/f5RVrHo+n07Htx6ekpJCUlNTt+bo7h4iIiMixbA1M7UNjVVVVHbZXVVV1Ofm6sLCw07GBQID6+nry8/PJysoiJSXlc8/X3TlEREREjmVrYJo0aRJpaWmsWbMmtq2xsZGtW7dSUlLS6fiSkhIqKio4cOBAbNvatWsBmDVrFoZhMHPmzNi2dmvWrOHMM8/s0TlEREREjmVrYHK73SxcuJBHH32Ut99+m+3bt3PLLbdQWFjIxRdfTDgcprq6OjY3afr06cycOZNbbrmFzZs3s3r1au677z7mz58f60H613/9V/70pz/x61//mj179vBf//VfbNu2jUWLFvX4HCIiIiJHMyybV8UKh8P85Cc/4ZVXXsHn88VW+i4uLqa0tJQvfOELPPjggyxYsACAmpoali1bxvvvv09SUhKXXHIJd999d2z+EsCrr77Kk08+SUVFBePHj2fp0qUdli7oyTlERERE2tkemEREREQSne5VISIiItINBSYRERGRbigwiYiIiHRDgUlERESkGwpMIiIiIt1QYBIRERHphgKTiIiISDcUmOSk7Nu3jzPOOINXXnkltm3btm0sXLiQGTNmcOGFF/Kb3/zGxgoT36uvvsqll17K6aefzmWXXcaf//zn2L7S0lJuuOEGZs6cyXnnncdPf/pTwuGwjdUmrlAoxOOPP84FF1zAGWecwdVXX83HH38c26/PZfd++ctf8q1vfavDtu7aLRKJsHz5cubOncuMGTO47rrrOHToUH+WnZC6ast33nmHr3/965xxxhlceOGFPPzww7E7WUD0JvDLli1jzpw5nHHGGdx2223U1tb2d+kJpat2PNq9997LhRde2GFbn30mLZFeCgQC1oIFC6wJEyZYL7/8smVZllVbW2udddZZ1t13323t3r3b+v3vf2+dfvrp1u9//3ubq01Mr776qjVlyhTrd7/7nXXgwAHrySeftCZNmmR99NFHViAQsC6++GLr+uuvt3bs2GH99a9/tWbPnm09/vjjdpedkJYvX26de+651vvvv2/t37/fuueee6xZs2ZZlZWV+lz2wO9+9ztr0qRJ1sKFC2PbetJuP/vZz6yzzjrLevfdd61t27ZZ1157rXXxxRdbfr/fjreRELpqy3Xr1lmTJ0+2nnrqKWvfvn3W3/72N2vevHnWXXfdFTvmrrvusi666CJr3bp11qZNm6z58+dbV199tR1vISF01Y5H++tf/2pNmDDBuuCCCzps76vPpAKT9NqPf/xj69vf/naHwPSLX/zCOu+886xgMNjhuIsvvtiuMhNWJBKxLrjgAuuhhx7qsP3aa6+1fvGLX1grV660TjvtNKu+vj6274UXXrBmzpw5pH8YHc9XvvIV68EHH4z9f1NTkzVhwgTrjTfe0Ofyc1RUVFg33HCDNWPGDOuSSy7p8MOpu3bz+/3WGWecYf3P//xPbH9DQ4M1bdo0a+XKlf33JhLE57XlbbfdZl1zzTUdjv/DH/5gTZ061fL7/VZFRYU1adIk629/+1ts/969e60JEyZYH330Ub+9h0Twee3YrrKy0jr77LOthQsXdghMffmZ1JCc9Mq6det48cUXeeihhzpsX79+PbNnz8bpdMa2nX322ezfv58jR470d5kJbd++fRw+fJgvf/nLHbY/88wz3HDDDaxfv56pU6eSmZkZ23f22WfT3NzMtm3b+rvchJebm8u7775LaWkp4XCYF198EbfbzaRJk/S5/BxbtmzB5XLxxz/+kenTp3fY1127bd++nZaWlg736szIyGDKlCmsW7eu395Dovi8trz22mu58847O2wzTZNgMEhzczMbNmwAou3bbuzYsRQUFAy5tvy8dgSwLIu77rqLr371q8yePbvDvr78TDq7P0Sko8bGRu644w7uvfdeioqKOuyrqKhgwoQJHbbl5+cDUF5ezrBhw/qtzkS3b98+AFpbW/nOd77D1q1bKS4u5sYbb+TCCy+koqKCwsLCDs85ui27+kYylN1zzz38+7//O1/4whdwOByYpsnPfvYzRo0apc/l57jwwgs7zQFp1127VVRUAHT6PpCfnx/bN5R8XltOmTKlw/8Hg0FWrFjBaaedRk5ODpWVlWRnZ3e6CfxQbMvPa0eAFStWUF1dzS9+8Qt++ctfdtjXl59J9TDJCbv//vs544wzOvWMAPh8Ptxud4dt7d8A/H5/v9Q3UDQ3NwNw5513cvnll/Pss89y7rnnctNNN7Fq1Sq15QnavXs36enp/PznP+fFF19kwYIF3H777Wzbtk1t2UvdtZvX6wXo8hi16/GFQiHuuOMOdu3axX/8x38A4PV6O7UjqC2PtX37dp544gkeeeSRLturLz+T6mGSE/Lqq6+yfv16Vq5c2eV+j8dDIBDosK39Q5qSktLn9Q0kLpcLgO985zt87WtfA2Dy5Mls3bqVX//612rLE1BeXs5tt93GihUrOPPMMwE4/fTT2b17Nz/72c/Ulr3UXbt5PB4AAoFA7O/txyQnJ/dfoQNIc3MzN998M2vXruWJJ55g2rRpQNdtDWrLo/n9fm6//XZuvPFGJk2a1OUxffmZVGCSE/Lyyy9TU1PD+eef32H7f/zHf/D6669TWFhIVVVVh33t/19QUNBfZQ4I7e1x7JDH+PHj+dvf/sbs2bPZuXNnh31qy65t2rSJYDDI6aef3mH79OnTee+99xg+fLg+l73Q3ddzKBSKbRs1alSHYyZOnNh/hQ4QVVVVXHfddRw+fJhnnnmGkpKS2L7CwkLq6+sJBAIdekeqqqr0GW2zadMmdu3axRNPPMHPf/5zIDq0GQqFOOOMM/jVr34VG4rri8+kApOckEcffbTDuiEAF198MUuWLOErX/kKr732Gi+88ALhcBiHwwHA6tWrGTt2LLm5uXaUnLCmTp1KamoqmzZtivWKAOzcuZNRo0ZRUlLCq6++SnNzM2lpaUC0LVNTU4/729VQ1T7Xa8eOHbHf2CHalmPGjGH69On6XPZCSUnJ57Zbeno6aWlprFmzJvbDqbGxka1bt7Jw4UI7S084DQ0NLFq0iObmZv7nf/6n0w/vWbNmEYlE2LBhQ2zC8r59+6isrOwQrIayadOm8eabb3bY9tvf/pY333yT3/72txQUFGCaZp99JjWHSU5IQUEBo0eP7vCA6BVKBQUFfP3rX6e5uZl77rmH3bt388orr7BixQpuuOEGmytPPB6Ph8WLF/Pzn/+c//u//+PgwYM89dRTfPjhh/zrv/4rF110EXl5edx8881s376dt956i5/85Cdce+21XY7dD2XTpk1j1qxZ3HnnnaxevZr9+/fz05/+lFWrVnH99dfrc9lL3bWb2+1m4cKFPProo7z99tts376dW265hcLCQi6++GKbq08sDz74IIcOHeKRRx4hJyeH6urq2CMcDlNQUMBll13Gvffey5o1a9i8eTO33nors2fPZsaMGXaXnxA8Hk+nnz+ZmZk4nU5Gjx6Nx+Pp08+kepgkrnJzc3n66af54Q9/yNe+9jXy8vK44447YnN0pKObbrqJ5ORkHnvsMSorKznllFP42c9+xllnnQXA008/zbJly/jmN79JZmYmV111FTfddJPNVSce0zR56qmn+OlPf8rdd99NQ0MDEyZMYMWKFbGrCfW5PHE9+XpesmQJoVCIe++9F5/PR0lJCc8880xsjp5AOBzm9ddfJxgMsmjRok773377bYqLi/nBD37Aj370I/7t3/4NgHnz5nHvvff2d7kDXl99Jg3Lsqw41SgiIiIyKGlITkRERKQbCkwiIiIi3VBgEhEREemGApOIiIhINxSYRERERLqhwCQiIiLSDQUmERGbaFUXkYFDgUlEBqx///d/jy3yebRPPvmEiRMnMnPmTILBYId9n376KRMnTuTVV1/t9vylpaVMnDiRV155pcc19fQ5b7/9NnfeeWePzysi9lJgEpEBa86cOdTX17N3794O299//32ysrJoaWlh48aNHfatX78egHPPPbfb8+fn5/Piiy92utl0PKxYsYLy8vK4n1dE+oYCk4gMWO03Kf3oo486bP/ggw+45JJLGD58OO+//36HfevWrWPChAnk5eV1e363282MGTPIycmJX9EiMiApMInIgDV69GhGjBjRITA1NTWxadMmzjnnHObMmcMHH3zQ4TkbNmyI9S6VlZXFbnA6ffp0Fi1axNatW2PHdjW8tnHjRq6++mpmzJjB+eefz3//939zzTXXcNddd3V4nerqapYsWcIZZ5zB7Nmz+f73v09LSwsA3/rWt1i7di1r165l4sSJrFmzJu5tIyLxpcAkIgPa2Wef3SEwrVq1CsuymDNnDueddx7btm3jyJEjAOzevZu6ujrOPfdcamtrueKKK9iyZQvf//73+fGPf0wkEuHqq69mz549Xb7Wnj17uOaaawD4yU9+wve+9z3+3//7f2zYsKHTsY8//jhFRUU8+eSTLFq0iP/93//liSeeAOA//uM/mDJlClOmTOHFF19k6tSpcW4VEYk3p90FiIicjDlz5vDyyy9TW1tLTk4O77//PtOmTSMjI4NzzjkHwzD44IMPmD9/PuvWrcPtdlNSUsJTTz1FfX09zz//PCNGjACid4e/9NJLefzxx1m+fHmn1/rlL39Jeno6Tz/9NMnJyQCMGzeOK664otOxX/rSl7j77rtjNX744YesXr0agPHjx5OWlgbAjBkz+qJZRCTO1MMkIgNa+zym9sndH3zwAeeddx4AWVlZTJ06lX/84x9AdML3zJkz8Xg8rFq1ismTJ1NQUEAoFCIUCmGaJvPmzYsdf6zVq1czb968WFgCOOOMM2KB62hnnnlmh/8vLi6msbHx5N+wiNhCPUwiMqANGzaMCRMm8NFHHzFmzBjKysqYO3dubP+5554bW0Jgw4YNXHXVVQDU19dz4MCB4w6Heb3eTttqa2vJzc3tsoZjHR2qAEzT1LpLIgOYApOIDHhnn302mzZtoqioiKysLE4//fTYvvPOO49f/OIXrF69mvLy8tiE7/T0dGbPns0dd9zR5TndbnenbYWFhbH5UEerqalh3LhxcXo3IpKINCQnIgPeOeecw5YtW1izZg1z5szBND/71jZjxgxSU1N57rnnyM7OZsqUKQDMnj2bffv2MXbsWE4//fTY47XXXuP3v/89Doej0+uUlJTw/vvv4/f7Y9u2bt1KaWnpCdd8dI0ikvj0FSsiA15JSQmBQIB33303Nn+pncvlYvbs2bzzzjuxSeAA11xzDZFIhGuuuYbXX3+dVatW8f3vf5/f/va3jB07tsvX+e53v0tTUxOLFy/m3Xff5bXXXuPf/u3fME0zdt6eysjIYN++faxatYqGhobevXER6TcKTCIy4KWlpXH66acTDAY7BSaAuXPnEgwGOeecc2LbCgoKeOGFFxgxYgT3338/3/3ud9m8eTM//OEPY0sHHGv06NE888wz+P1+lixZwmOPPcZ1111HXl4eqampJ1Tz1Vdfjcvl4rrrruO99947oeeKSP8zLM1CFBHpkVWrVuFyuTpcAdfY2Mg555zDHXfcwbe//W0bqxORvqRJ3yIiPbRlyxaWL1/OrbfeytSpU6mvr+fXv/416enpXH755XaXJyJ9SIFJRKSHrr32WgKBAM8//zzl5eWkpKQwe/ZsHnzwQd1vTmSQ05CciIiISDc06VtERESkGwpMIiIiIt1QYBIRERHphgKTiIiISDcUmERERES6ocAkIiIi0g0FJhEREZFuKDCJiIiIdEOBSURERKQb/x/GOWMtpksGowAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# finding the distribution of \"Weight\" column\n",
    "sns.distplot(calories_data['Weight'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f2aeaef-5bd1-4a49-b723-848de80d29c7",
   "metadata": {},
   "source": [
    "Finding the Correlation in the dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2cd5f8a5-5059-4cd7-bd2d-905e126e953d",
   "metadata": {},
   "source": [
    "1.Positive Correlation \n",
    "2.Negative Correlation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "e51b88c8-8c1e-4fe5-a579-6e8d47330c8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "correlation = calories_data.corr() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "47d4fc93-a472-4d5b-a888-bc2b4cd8b62e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Tp3CnTt3cPPmTSxcuFDoOERERERERG+llIXVpk2bkJCQgLlz58La2lrafvz4ccyYMeOtzx02bBjGj1fOqwZERERERKSalLKw2rt3b7ntbdu2RWho6Fuf+1/NHvhPvbzXioiIiIhIGajw8oBKSSkLq4oYGhrC0NDw3TsSEREREZFaKiwsxA8//IATJ06goKAA3t7emDFjBszNzd/r+WvXrsWyZcv+cccJb/EmIiIiIiKVMXv2bFy8eBErV67E9u3bcf/+/fe+VSgqKgqrVq36Vz+XhRURERERkQoSeg1gIdYHTk1NRWhoKGbOnAk3Nzc4OTlhyZIlCA8Px40bb5/lMy8vD99++y3c3Nz+1c9mYUVERERERCohIiICANCyZUtpW506dWBlZYXw8PC3PjcoKAgODg7o1q3bv/rZH9U9VkRERERE9PFr3779W7efPn36X71uamoqzMzMoKurK9NerVo1PHnypMLnnTx5EufOncPRo0dx9uzZf/WzWVgREREREakiFZwV8PHjx28tyiZMmAAdHR25dl1dXRQWFpb7nNTUVAQEBGDhwoUwMzP719lYWBERERERkUL92x4pKysrHD9+vMLt586dQ1FRkVx7YWEh9PX15dolEgmmTZuGL774Am3atPlXmV5iYUVERERERB8FbW1t2NvbV7j97t27yMzMRFFRkUzP1dOnT2FlZSW3f3JyMv744w9ERkZK18stKSkBALi4uCAwMBBdu3Z9r2wsrIiIiIiIVJBIFccCvkOzZs0gFosREREBDw8PAEBCQgJSU1PRvHlzuf2trKxw8uRJmbaTJ09i0aJFCA0NhYWFxXv/bBZWRERERESkEqysrNC5c2fMnDkTwcHB0NfXx6xZs9CiRQs4OzsDAIqKipCVlQUTExPo6OjAzs5O5jVeFlNvtr8Lp1snIiIiIiKVMXfuXHh4eGDcuHHw8/ND3bp1sWLFCun2GzduwMvL653rWv1TIolEIvlPX5H+U0Gn7wkdQemoY7f225SI+RZ+kyYvGcnhaSIveM6PQkdQPpY2QidQPgn/7RcvlVDDQegESic/bLzQEcp181GO0BEq5GxrJHSE/xy/fhAREREREVUSCysiIiIiIqJK4uQVREREREQqiDdPKBZ7rIiIiIiIiCqJhRUREREREVElcSggEREREZEq4lhAhWKPFRERERERUSWxsCIiIiIiIqokDgUkIiIiIlJBIo4FVCj2WBEREREREVUSCysiIiIiIqJK4lBAIiIiIiIVJOJIQIVijxUREREREVElsbAiIiIiIiKqJA4FpI+OFi8HyLifViB0BKVja64ndASlU1wqETqC8il8IXQC5fM8SegEyqeGg9AJlE9ynNAJ6D1xJKBi8SsqERERERFRJbGwIiIiIiIiqiQOBSQiIiIiUkUcC6hQ7LEiIiIiIiKqJBZWRERERERElcShgEREREREKkjEsYAKxR4rIiIiIiKiSmJhRUREREREVEkcCkhEREREpIJEHAmoUOyxIiIiIiIiqiQWVkRERERERJXEoYBERERERCqIIwEViz1WRERERERElcTCioiIiIiIqJI4FJCIiIiISBVxLKBCsceKiIiIiIioklhYERERERERVRKHAhIRERERqSARxwIqFHusiIiIiIiIKomFFRERERERUSVxKCARERERkQoScSSgQrHHioiIiIiIqJJYWBEREREREVUShwISEREREakgjgRULPZYERERERERVRILKyIiIiIiokriUEAiIiIiIlXEsYAKpZQ9ViUlJdi+fTt69uwJFxcXtGzZEsOHD8eVK1fe+zVWrlwJb2/vSuU4ePAgGjRoUKnXICIiIiIi1ad0PVaFhYUYNmwYUlJSMH78eLi4uKCgoAA///wzhg0bhoULF6JLly4KydKpUye0bt1aIT+LiIiIiIg+XkpXWC1fvhx3797FsWPHYG1tLW2fMWMGcnNzMW/ePHh7e8PQ0PCDZ9HT04Oent4H/znKJvLwdjy6+QcgkaBZTz/YOLnL7fMkLhrhB9ajpKgQ1g2c0aLPKGhoagqQVjGuh27Dgxt/AJCgRa8RsC3nmKTERePK/vUoKSpADUdnePQdrbLHpFktY3RtXA1aGiJceZiJo7eeyWy3NdPDANca0NUSoahEgp0RyXicWSBQ2g/vYeQFRB/fDXFpCWo3bwenTgNktudlpuGP7YuQn50BfRNzeA2bCj0jU2HCKkjijYu4dWI3xCXFsHNrh0++kD8mV3cuRkFOBvSNzdFyyHcqf0wAwMhQF2c2jEWvKVvxKCVDZlujulZYO6M3TKro4/b9JxgRuBd5BcUCJVWMnp82xIyhbaGjrYk9J6MRvP28zHY3xxpYNukL6GhrITE1C2NCjiI1/YVAaRWjp1c9zBjgDh0t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",
      "text/plain": [
       "<Figure size 1000x1000 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#constructing a heatmap to understand the correlation\n",
    "\n",
    "plt.figure(figsize=(10,10)) \n",
    "sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a70d39fe-cd70-4136-840a-e8f554b71c81",
   "metadata": {},
   "source": [
    "Converting the text data to numerical values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "a95a1e19-6e3d-422a-9624-4d91350aeaca",
   "metadata": {},
   "outputs": [],
   "source": [
    "calories_data.replace({\"Gender\":{'male':0,'female':1}}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "ed8dea1f-0870-4460-ab15-6ed388178780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>User_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Heart_Rate</th>\n",
       "      <th>Body_Temp</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>14733363</td>\n",
       "      <td>0</td>\n",
       "      <td>68</td>\n",
       "      <td>190.0</td>\n",
       "      <td>94.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>105.0</td>\n",
       "      <td>40.8</td>\n",
       "      <td>231.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14861698</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>166.0</td>\n",
       "      <td>60.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>94.0</td>\n",
       "      <td>40.3</td>\n",
       "      <td>66.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11179863</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>179.0</td>\n",
       "      <td>79.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>38.7</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16180408</td>\n",
       "      <td>1</td>\n",
       "      <td>34</td>\n",
       "      <td>179.0</td>\n",
       "      <td>71.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>40.5</td>\n",
       "      <td>71.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>17771927</td>\n",
       "      <td>1</td>\n",
       "      <td>27</td>\n",
       "      <td>154.0</td>\n",
       "      <td>58.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>81.0</td>\n",
       "      <td>39.8</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    User_ID  Gender  Age  Height  Weight  Duration  Heart_Rate  Body_Temp  \\\n",
       "0  14733363       0   68   190.0    94.0      29.0       105.0       40.8   \n",
       "1  14861698       1   20   166.0    60.0      14.0        94.0       40.3   \n",
       "2  11179863       0   69   179.0    79.0       5.0        88.0       38.7   \n",
       "3  16180408       1   34   179.0    71.0      13.0       100.0       40.5   \n",
       "4  17771927       1   27   154.0    58.0      10.0        81.0       39.8   \n",
       "\n",
       "   Calories  \n",
       "0     231.0  \n",
       "1      66.0  \n",
       "2      26.0  \n",
       "3      71.0  \n",
       "4      35.0  "
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calories_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ba0eed0-31c3-4d04-b600-747eba730c51",
   "metadata": {},
   "source": [
    "Separating features and Target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "9c2e18de-995b-4e7f-a8ee-f5410fb12877",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = calories_data.drop(columns=['User_ID','Calories'], axis=1)\n",
    "Y = calories_data['Calories']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "24094a2a-5406-4427-8998-067c8abe9d70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Gender  Age  Height  Weight  Duration  Heart_Rate  Body_Temp\n",
      "0           0   68   190.0    94.0      29.0       105.0       40.8\n",
      "1           1   20   166.0    60.0      14.0        94.0       40.3\n",
      "2           0   69   179.0    79.0       5.0        88.0       38.7\n",
      "3           1   34   179.0    71.0      13.0       100.0       40.5\n",
      "4           1   27   154.0    58.0      10.0        81.0       39.8\n",
      "...       ...  ...     ...     ...       ...         ...        ...\n",
      "14995       1   20   193.0    86.0      11.0        92.0       40.4\n",
      "14996       1   27   165.0    65.0       6.0        85.0       39.2\n",
      "14997       1   43   159.0    58.0      16.0        90.0       40.1\n",
      "14998       0   78   193.0    97.0       2.0        84.0       38.3\n",
      "14999       0   63   173.0    79.0      18.0        92.0       40.5\n",
      "\n",
      "[15000 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "print(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "258729f3-18c8-4f57-bb11-1ab148136ea6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0        231.0\n",
      "1         66.0\n",
      "2         26.0\n",
      "3         71.0\n",
      "4         35.0\n",
      "         ...  \n",
      "14995     45.0\n",
      "14996     23.0\n",
      "14997     75.0\n",
      "14998     11.0\n",
      "14999     98.0\n",
      "Name: Calories, Length: 15000, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(Y)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d53cc79-09fd-4375-bed9-aff1d9c38e94",
   "metadata": {},
   "source": [
    "Splitting the data into training data and Test data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "0add001e-a173-4dc1-ad0c-e3730c15fb7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "8303c312-9159-4edf-9690-b8de2ed120ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(15000, 7) (12000, 7) (3000, 7)\n"
     ]
    }
   ],
   "source": [
    "print(X.shape, X_train.shape, X_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f3df4ae-8c35-46de-8cb3-201f56be2608",
   "metadata": {},
   "source": [
    "Model Training"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa79e671-ecaa-4a0c-91c2-38c7d461e995",
   "metadata": {},
   "source": [
    "XGBoost Regressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "f24c77c3-1279-44e4-b0ea-82c7cce6bbbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the model\n",
    "model = XGBRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "10bf3ae2-e6d7-41c9-abea-ad85f76961bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: black;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-3 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-3 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-3 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: block;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-3 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-3 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-3 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-3 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-3 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 1ex;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-3 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-3 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
       "             colsample_bylevel=None, colsample_bynode=None,\n",
       "             colsample_bytree=None, device=None, early_stopping_rounds=None,\n",
       "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
       "             gamma=None, grow_policy=None, importance_type=None,\n",
       "             interaction_constraints=None, learning_rate=None, max_bin=None,\n",
       "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
       "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
       "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
       "             multi_strategy=None, n_estimators=None, n_jobs=None,\n",
       "             num_parallel_tree=None, random_state=None, ...)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;XGBRegressor<span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></label><div class=\"sk-toggleable__content fitted\"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
       "             colsample_bylevel=None, colsample_bynode=None,\n",
       "             colsample_bytree=None, device=None, early_stopping_rounds=None,\n",
       "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
       "             gamma=None, grow_policy=None, importance_type=None,\n",
       "             interaction_constraints=None, learning_rate=None, max_bin=None,\n",
       "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
       "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
       "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
       "             multi_strategy=None, n_estimators=None, n_jobs=None,\n",
       "             num_parallel_tree=None, random_state=None, ...)</pre></div> </div></div></div></div>"
      ],
      "text/plain": [
       "XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
       "             colsample_bylevel=None, colsample_bynode=None,\n",
       "             colsample_bytree=None, device=None, early_stopping_rounds=None,\n",
       "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
       "             gamma=None, grow_policy=None, importance_type=None,\n",
       "             interaction_constraints=None, learning_rate=None, max_bin=None,\n",
       "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
       "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
       "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
       "             multi_strategy=None, n_estimators=None, n_jobs=None,\n",
       "             num_parallel_tree=None, random_state=None, ...)"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# training the model with X_train\n",
    "model.fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2732930-6ac4-4a26-85c3-52fec249b1b8",
   "metadata": {},
   "source": [
    "Evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "664c2448-36b0-43c9-b1de-a9cb53966adf",
   "metadata": {},
   "source": [
    "Prediction on Test Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "9318e5f7-74d5-4c1d-bd4b-946d38964d39",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data_prediction = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "20f0e92d-c345-4434-8a8c-332ee7af7785",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[125.58828  222.11377   38.725952 ... 144.3179    23.425894  90.100494]\n"
     ]
    }
   ],
   "source": [
    "print(test_data_prediction)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52e7d650-7ddb-4a20-bfea-b933645023f9",
   "metadata": {},
   "source": [
    "Mean Absolute Error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "889a1435-a3f3-409c-949c-2516a910f531",
   "metadata": {},
   "outputs": [],
   "source": [
    "mae = metrics.mean_absolute_error(Y_test, test_data_prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "e4b2a768-e0e7-4641-b0bd-0836fac51187",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error =  1.4833678883314132\n"
     ]
    }
   ],
   "source": [
    "print(\"Mean Absolute Error = \", mae)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c77448f-0526-42c4-825d-7dacccdd5e0f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "741242db-0196-458a-b072-e245e5b819c6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
