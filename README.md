{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.026943,
          "end_time": "2020-12-11T03:31:51.129184",
          "exception": false,
          "start_time": "2020-12-11T03:31:51.102241",
          "status": "completed"
        },
        "tags": [],
        "id": "9DUc-XB_h2g4"
      },
      "source": [
        " **HEART DISEASE ANALYSIS** "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.023267,
          "end_time": "2020-12-11T03:31:51.177448",
          "exception": false,
          "start_time": "2020-12-11T03:31:51.154181",
          "status": "completed"
        },
        "tags": [],
        "id": "5j3um47lh2g-"
      },
      "source": [
        "## **About Heart Disease**\n",
        "\n",
        "> Cardiovascular disease or heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease. From WHO statistics every year 17.9 million dying from heart disease. The medical study says that human life style is the main reason behind this heart problem. Apart from this there are many key factors which warns that the person may/may not getting chance of heart disease.\n",
        "\n",
        "\n",
        "> From the dataset we will create suitable machine learning technique which classify the heart disease more accurately, it is very helpful to the health organisation as well as patients. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.023238,
          "end_time": "2020-12-11T03:31:51.319392",
          "exception": false,
          "start_time": "2020-12-11T03:31:51.296154",
          "status": "completed"
        },
        "tags": [],
        "id": "pGWTTQPzh2hD"
      },
      "source": [
        "#**Packages and dataset description**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.02368,
          "end_time": "2020-12-11T03:31:51.225094",
          "exception": false,
          "start_time": "2020-12-11T03:31:51.201414",
          "status": "completed"
        },
        "tags": [],
        "id": "c28YJ606h2hA"
      },
      "source": [
        "## **About the Data set**\n",
        "> This dataset gives the information realated to heart disease. Dataset contain 13 columns, target is the class variable which is affected by other 12 columns. Here the aim is to classify the target variable to (disease\\non disease) using different machine learning algorithm and findout which algorithm suitable for this dataset.\n",
        "\n",
        "> **Attribute Information**\n",
        "> * Age (age in years)\n",
        "> * Sex (1 = male; 0 = female)\n",
        "> * CP (chest pain type)\n",
        "> * TRESTBPS (resting blood pressure (in mm Hg on admission to the hospital))\n",
        "> * CHOL (serum cholestoral in mg/dl)\n",
        "> * FBS (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)\n",
        "> * RESTECH (resting electrocardiographic results)\n",
        "> * THALACH (maximum heart rate achieved)\n",
        "> * EXANG (exercise induced angina (1 = yes; 0 = no))\n",
        "> * OLDPEAK (ST depression induced by exercise relative to rest)\n",
        "> * SLOPE (the slope of the peak exercise ST segment)\n",
        "> * CA (number of major vessels (0-3) colored by flourosopy)\n",
        "> * THAL (defect-Reversible/Fixed/Normal)\n",
        "> * TARGET (1=heart disease or 0=disease free heart)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rKRoECsOocdl",
        "outputId": "bce47108-c992-45e4-81fb-da1e55165e5e"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:31:51.383924Z",
          "iopub.status.busy": "2020-12-11T03:31:51.381244Z",
          "iopub.status.idle": "2020-12-11T03:31:55.003384Z",
          "shell.execute_reply": "2020-12-11T03:31:55.002244Z"
        },
        "papermill": {
          "duration": 3.659744,
          "end_time": "2020-12-11T03:31:55.003569",
          "exception": false,
          "start_time": "2020-12-11T03:31:51.343825",
          "status": "completed"
        },
        "tags": [],
        "id": "LdQDCQ3Xh2hE"
      },
      "outputs": [],
      "source": [
        "#loading dataset\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "#visualisation\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "import seaborn as sns\n",
        "#EDA\n",
        "from collections import Counter\n",
        "# data preprocessing\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.preprocessing import minmax_scale\n",
        "# data splitting\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.model_selection import KFold\n",
        "# data modeling\n",
        "from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report,recall_score\n",
        "from sklearn.metrics import f1_score\n",
        "from sklearn.metrics import precision_score\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "from xgboost import XGBClassifier\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "from sklearn.svm import SVC\n",
        "from sklearn.ensemble import StackingClassifier\n",
        "from sklearn.svm import LinearSVC\n",
        "#warning\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "_cell_guid": "79c7e3d0-c299-4dcb-8224-4455121ee9b0",
        "_uuid": "d629ff2d2480ee46fbb7e2d37f6b5fab8052498a",
        "execution": {
          "iopub.execute_input": "2020-12-11T03:31:55.074081Z",
          "iopub.status.busy": "2020-12-11T03:31:55.073215Z",
          "iopub.status.idle": "2020-12-11T03:31:55.112201Z",
          "shell.execute_reply": "2020-12-11T03:31:55.112835Z"
        },
        "papermill": {
          "duration": 0.084306,
          "end_time": "2020-12-11T03:31:55.113016",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.028710",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "pfrePQVTh2hI",
        "outputId": "627b5b5a-cc3e-4cde-d1c5-42dd653d287e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \\\n",
              "0   52    1   0       125   212    0        1      168      0      1.0      2   \n",
              "1   53    1   0       140   203    1        0      155      1      3.1      0   \n",
              "2   70    1   0       145   174    0        1      125      1      2.6      0   \n",
              "3   61    1   0       148   203    0        1      161      0      0.0      2   \n",
              "4   62    0   0       138   294    1        1      106      0      1.9      1   \n",
              "\n",
              "   ca  thal  target  \n",
              "0   2     3       0  \n",
              "1   0     3       0  \n",
              "2   0     3       0  \n",
              "3   1     3       0  \n",
              "4   3     2       0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-57df5bcb-4a7a-4195-a7d9-f6756d819d1a\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>52</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>125</td>\n",
              "      <td>212</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>168</td>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>53</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>140</td>\n",
              "      <td>203</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>155</td>\n",
              "      <td>1</td>\n",
              "      <td>3.1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>70</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>145</td>\n",
              "      <td>174</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>125</td>\n",
              "      <td>1</td>\n",
              "      <td>2.6</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>148</td>\n",
              "      <td>203</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>161</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>62</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>138</td>\n",
              "      <td>294</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>106</td>\n",
              "      <td>0</td>\n",
              "      <td>1.9</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-57df5bcb-4a7a-4195-a7d9-f6756d819d1a')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-57df5bcb-4a7a-4195-a7d9-f6756d819d1a button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-57df5bcb-4a7a-4195-a7d9-f6756d819d1a');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "data = pd.read_csv('/content/drive/MyDrive/content/heart.csv')\n",
        "data.head()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.shape\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n5tn9Ge0I__A",
        "outputId": "655fc58b-1416-4d65-810f-6bec6ab7c588"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1025, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:31:55.187977Z",
          "iopub.status.busy": "2020-12-11T03:31:55.182700Z",
          "iopub.status.idle": "2020-12-11T03:31:55.205942Z",
          "shell.execute_reply": "2020-12-11T03:31:55.205197Z"
        },
        "papermill": {
          "duration": 0.066446,
          "end_time": "2020-12-11T03:31:55.206102",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.139656",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2ZS5-p3Bh2hL",
        "outputId": "e75cd67d-74fd-46f4-8af9-aa13c21cc1d0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1025 entries, 0 to 1024\n",
            "Data columns (total 14 columns):\n",
            " #   Column    Non-Null Count  Dtype  \n",
            "---  ------    --------------  -----  \n",
            " 0   age       1025 non-null   int64  \n",
            " 1   sex       1025 non-null   int64  \n",
            " 2   cp        1025 non-null   int64  \n",
            " 3   trestbps  1025 non-null   int64  \n",
            " 4   chol      1025 non-null   int64  \n",
            " 5   fbs       1025 non-null   int64  \n",
            " 6   restecg   1025 non-null   int64  \n",
            " 7   thalach   1025 non-null   int64  \n",
            " 8   exang     1025 non-null   int64  \n",
            " 9   oldpeak   1025 non-null   float64\n",
            " 10  slope     1025 non-null   int64  \n",
            " 11  ca        1025 non-null   int64  \n",
            " 12  thal      1025 non-null   int64  \n",
            " 13  target    1025 non-null   int64  \n",
            "dtypes: float64(1), int64(13)\n",
            "memory usage: 112.2 KB\n"
          ]
        }
      ],
      "source": [
        "data.info()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.029017,
          "end_time": "2020-12-11T03:31:55.267778",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.238761",
          "status": "completed"
        },
        "tags": [],
        "id": "nMZzZL52h2hM"
      },
      "source": [
        "### **Missing Value Detection**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:31:55.347133Z",
          "iopub.status.busy": "2020-12-11T03:31:55.346172Z",
          "iopub.status.idle": "2020-12-11T03:31:55.351411Z",
          "shell.execute_reply": "2020-12-11T03:31:55.350699Z"
        },
        "papermill": {
          "duration": 0.046825,
          "end_time": "2020-12-11T03:31:55.351539",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.304714",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9F2-hrjCh2hN",
        "outputId": "4859b73d-7480-4a8f-bd73-45eaa683a20d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "age         0\n",
              "sex         0\n",
              "cp          0\n",
              "trestbps    0\n",
              "chol        0\n",
              "fbs         0\n",
              "restecg     0\n",
              "thalach     0\n",
              "exang       0\n",
              "oldpeak     0\n",
              "slope       0\n",
              "ca          0\n",
              "thal        0\n",
              "target      0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "data.isnull().sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.026595,
          "end_time": "2020-12-11T03:31:55.405201",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.378606",
          "status": "completed"
        },
        "tags": [],
        "id": "hwcgScVbh2hO"
      },
      "source": [
        "### **Descriptive statistics**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:31:55.476200Z",
          "iopub.status.busy": "2020-12-11T03:31:55.475299Z",
          "iopub.status.idle": "2020-12-11T03:31:55.536881Z",
          "shell.execute_reply": "2020-12-11T03:31:55.536197Z"
        },
        "papermill": {
          "duration": 0.105649,
          "end_time": "2020-12-11T03:31:55.537024",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.431375",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 344
        },
        "id": "231Y57h4h2hP",
        "outputId": "cfe07688-7958-4e9c-f74d-3d1840f5831c"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "               age          sex           cp     trestbps        chol  \\\n",
              "count  1025.000000  1025.000000  1025.000000  1025.000000  1025.00000   \n",
              "mean     54.434146     0.695610     0.942439   131.611707   246.00000   \n",
              "std       9.072290     0.460373     1.029641    17.516718    51.59251   \n",
              "min      29.000000     0.000000     0.000000    94.000000   126.00000   \n",
              "25%      48.000000     0.000000     0.000000   120.000000   211.00000   \n",
              "50%      56.000000     1.000000     1.000000   130.000000   240.00000   \n",
              "75%      61.000000     1.000000     2.000000   140.000000   275.00000   \n",
              "max      77.000000     1.000000     3.000000   200.000000   564.00000   \n",
              "\n",
              "               fbs      restecg      thalach        exang      oldpeak  \\\n",
              "count  1025.000000  1025.000000  1025.000000  1025.000000  1025.000000   \n",
              "mean      0.149268     0.529756   149.114146     0.336585     1.071512   \n",
              "std       0.356527     0.527878    23.005724     0.472772     1.175053   \n",
              "min       0.000000     0.000000    71.000000     0.000000     0.000000   \n",
              "25%       0.000000     0.000000   132.000000     0.000000     0.000000   \n",
              "50%       0.000000     1.000000   152.000000     0.000000     0.800000   \n",
              "75%       0.000000     1.000000   166.000000     1.000000     1.800000   \n",
              "max       1.000000     2.000000   202.000000     1.000000     6.200000   \n",
              "\n",
              "             slope           ca         thal       target  \n",
              "count  1025.000000  1025.000000  1025.000000  1025.000000  \n",
              "mean      1.385366     0.754146     2.323902     0.513171  \n",
              "std       0.617755     1.030798     0.620660     0.500070  \n",
              "min       0.000000     0.000000     0.000000     0.000000  \n",
              "25%       1.000000     0.000000     2.000000     0.000000  \n",
              "50%       1.000000     0.000000     2.000000     1.000000  \n",
              "75%       2.000000     1.000000     3.000000     1.000000  \n",
              "max       2.000000     4.000000     3.000000     1.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-13f08417-ac96-405c-94c5-81e42448edfd\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.00000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "      <td>1025.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>54.434146</td>\n",
              "      <td>0.695610</td>\n",
              "      <td>0.942439</td>\n",
              "      <td>131.611707</td>\n",
              "      <td>246.00000</td>\n",
              "      <td>0.149268</td>\n",
              "      <td>0.529756</td>\n",
              "      <td>149.114146</td>\n",
              "      <td>0.336585</td>\n",
              "      <td>1.071512</td>\n",
              "      <td>1.385366</td>\n",
              "      <td>0.754146</td>\n",
              "      <td>2.323902</td>\n",
              "      <td>0.513171</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>9.072290</td>\n",
              "      <td>0.460373</td>\n",
              "      <td>1.029641</td>\n",
              "      <td>17.516718</td>\n",
              "      <td>51.59251</td>\n",
              "      <td>0.356527</td>\n",
              "      <td>0.527878</td>\n",
              "      <td>23.005724</td>\n",
              "      <td>0.472772</td>\n",
              "      <td>1.175053</td>\n",
              "      <td>0.617755</td>\n",
              "      <td>1.030798</td>\n",
              "      <td>0.620660</td>\n",
              "      <td>0.500070</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>29.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>94.000000</td>\n",
              "      <td>126.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>71.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>48.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>211.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>132.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>56.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>130.000000</td>\n",
              "      <td>240.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>152.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.800000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>61.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>140.000000</td>\n",
              "      <td>275.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>166.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.800000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>77.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>564.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>202.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.200000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-13f08417-ac96-405c-94c5-81e42448edfd')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-13f08417-ac96-405c-94c5-81e42448edfd button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-13f08417-ac96-405c-94c5-81e42448edfd');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "data.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.026543,
          "end_time": "2020-12-11T03:31:55.590824",
          "exception": false,
          "start_time": "2020-12-11T03:31:55.564281",
          "status": "completed"
        },
        "tags": [],
        "id": "7NGQ4ciCh2hQ"
      },
      "source": [
        "## **EDA**"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = data.target.value_counts().plot(kind = 'bar', color=[\"lightblue\", 'lightgreen'])\n",
        "fig.set_xticklabels(labels=['Has heart disease', \"Doesn't have heart disease\"], rotation=0);\n",
        "plt.title(\"Heart Disease values\")\n",
        "plt.ylabel(\"Number of people\");"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "id": "eFQzFD04FnGL",
        "outputId": "00d6370d-2f73-468b-8cb9-4b97d3229d85"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "labels = 'Male', 'Female'\n",
        "explode = (0, 0)\n",
        "\n",
        "fig1, ax1 = plt.subplots()\n",
        "ax1.pie(data.sex.value_counts(), explode=explode, labels=labels, autopct='%1.1f%%',\n",
        "        shadow=True, startangle=90)\n",
        "ax1.axis('equal')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 248
        },
        "id": "hou2KreTG5NG",
        "outputId": "569afcd0-0a3c-4952-d357-11f41cc30286"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAV0AAADnCAYAAAC9roUQAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deXzU1b3/8df5zpqZJJOEhH2JyIhsCiKMiguuWJC671Rrf7a117ba9uqly713ql1o671a76233rbW7brUfUHFfaUEBQULogEJ+xJCMklmX76/P76DooJknTPL5/l4zCMhzPIOZN45c+Z8z1eZpokQQojcMHQHEEKIUiKlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOSSlK4QQOWTXHUAIgPr5C23ASKAeqAVqgOrsxz2flwM2wPafjtvWnWN78yAgCSSyH5NAGNgEbAA2fvIxGErk8vsRYn+kdEVO1c9fOACYBowDDgbGZD+OAhxdvR9XKlyGjUAXr24S9G3n0xLe+7KCYGhT178DIXpHSlf0m/r5C8uBqVglu+dyUF/cd3s4NhJXl6+ugCHZyxeLOujbALwGvA68RjC0ti8yCrEvUrqiz9TPX2hgFevpwCzTNKcrpWz98Vg2Q/XldMEo4LLsBYK+rcAbfFrEqwmG5LxWok9I6YpeqZ+/sA6YA5xumuYpSqkBe/5OKaUvWO8MBS7MXgB2EfS9ATwP/I1gaLe2ZKLgSemKbqufv9ALnG2a5qXAKUopOxR0yR5ILXB29nILQd9TwJ3AcwRDaZ3BROGR0hVdUj9/oR1ryuBS4CylVFkRl+yXcQHnZS/bCfr+D/grwdAqvbFEoZDSFV+qfv7CQaZpfgfMf1LKqCvRot2fwcCPgB8R9C3DGv3eJ9MP4stI6Yp9qp+/cKqZTv0Iw3aeUsphLQAQX2Jq9vIf2emH2wmGXtCcSeQhKV3xifr5CxVwtplOzVc2+zRlkx+PHnAC5wLnEvQ1ADcQDD2jOZPII3IYsABg1HVPnGWmkh8AjyibfZruPEUiACwk6HuboO+rusOI/CBDmRI36ronZpmZ9E2GwzVRd5YidiTwBEHfcuDHBEPP6w4k9JHSLVGjrntihplJ/d5wuKfKNELOHAEsIuh7AbieYOg93YFE7smzrcSMuu7xoWYq8SfD5Z0tZavNqcBygr77gJ8RDDVpziNySOZ0S0T9/IX2Ed+791eg1hsu72zdeQQKuBT4gKDvnwn65LlYIuQ/ugQM/6c7T8rEIx/bvNU/Vja7U3ce8Rlu4HfAawR9B+sOI/qflG4RG/6dOzzDr777IVtF7UuGyzNCdx7xpY4FVhD0fUd3ENG/pHSL1JDL/vNUw1W+3l4x4Dw5iqxgeIHbCPoWEfQN1x1G9A8p3SJT99XrbUOv/J/bnYPHPGe4vQN15xE9chrwD4K+y3QHEX1PSreIDLr41xPdIw9b46wd+S1l2OT/trD5gLsI+h4j6JNfnkVEnphFwOMPqMHzfneVe9ih79jKq8foziP61FnAKjmirXhI6RY4jz9Q5jv6gvtcww69TdmdXT+BjSgktcBjBH0/1B1E9J6sji9gVcdeMrx65hULHQNGHKY7i+h3BtYOZvXAtQRDGc15RA/JSLdADTj9e8dWTJ69TAq35HwPeJSgz6M7iOgZKd0C4/EHVO3cf77SO/6E523l1fIGS2k6E3hF3mArTFK6BcTjDzg8hxx9o3fsjNsMZ1mZ7jxCq+nAEoK+Q3UHEd0jpVsgPP5AmWfsjNu840+cr+xOh+48Ii8cBCwm6DtOdxDRdVK6BcDjD1R4x8/8q3f8id9QNrtNdx6RV6qBFwj6LtIdRHSNlG6e8/gD1eWHzbrfc+hxFyjDkP8vsS8u4D6Cvn/SHUQcmDyJ85jHH6jzTjrlfo8/MEfJBgriyyngvwj6ztcdRHw5Kd085fEHhngOmXGnx3/0abqziIJhAPcQ9J2oO4jYPyndPOTxB2rdB039g3fCzNNlhCu6yQU8TtA3WXcQsW9SunnG4w9UuUZMvLni8FlzZdMa0UOVwLMEfQf19o6UUmml1Ht7Xep7nW7/j9WklKrtr/vPF/KkziMef6DcOeSQX1ceccYFymaXQ7RFbwzGOglmXS/vJ2qa5uS9Lk19kK2kSenmCY8/4LZV1M6vnPrVrym7U06pI/qCH1hI0OftyztVSk1VSr2mlFqmlFqklBqS/fqrSqmblVLvKKU+UEpNU0o9qpRqVEr9Yq/bP5697Sql1Lf28xjzlFJLs6Pr25VSRbNUUko3D3j8AbuyO6/2HXX+lYbL06dPEFHypgGPEPT19ICasr2mFh5TSjmA/wLOM01zKnAH8Mu9rp8wTfNI4I/AE8DVwETg60qpAdnrfCN72yOB7+/1dQCUUuOAC4EZpmlOBtJYJ/EsCvISVjOPP6CAcyqnn/Nte2XdIN15RFGaBdxB0HcZwZDZzdtGs8UHgFJqIlaJvpB9j9cGbNvr+k9mP74PrDJNc1v2dh8DI4AWrKI9O3u9EVgj8pa97uNkYCrwdvYxyoCd3cydt6R09TvKO+GkH7qGHOLXHUQUtXnAKmBBL+9HYZXp0fv5+3j2Y2avz/f82a6UmgmcAhxtmmZEKfUq1hmRP/8Yd5mm+eNeZs1LMr2gkccfGO0aPuFnnrHHTNOdRZSEGwn69leWXfUhUKeUOhpAKeVQSk3oxu19QGu2cA8FjtrHdV4CzlNKDcw+Ro1SalQvc+cNKV1NPP5Atc1b/S8VR5wxUyk5vFfkhB24n6Cvqqd3YJpmAjgP+I1SagXwHnBMN+7iOawR7wdYo+4l+3iM1cDPgOeVUiuBF4AhPc2cb2R6QQOPP+AErq4MnDvLcLhkM2qRS6OAP2MV5wGZplm+j6+9Bxy/j6/P3OvzV4FX9/V3wFf281j1e33+IPBgVzIWGhlh6THXO+HEOY7qoUXzkkkUlHMJ+r6jO0SpktLNMY8/cKi9Zvg8zyHHTNWdRZS0mwj65M1bDaR0c8jjD5Rj2L/jm37OMcqwyUbkQicPcCdBn3RAjsk/eI5k1+POqzhiznE2b5Wc20rkg2OAH+kOUWqkdHNnur1m+OnuEZPk7L0in9xI0Dded4hSIqWbAx5/oBq4onLq3MnKMIrmGHJRFFzAXTLNkDvyD93PstMKF3jGzvDbK+tktYLIR0cCX9MdolRI6fa/scrpOcEz9tjpuoMI8SVuIOhz6Q5RCqR0+1H2IIgrKo/86jjD4frCInMh8shI4Lu6Q5QCKd3+dbJjwMhDnIP9h+sOIkQX/ISgz6c7RLGT0u0nHn+gDji3fPKs8XKeM1EgaoD5ukMUOynd/nO2a+ihtY6qIYfoDiJEN1xD0DdUd4hiJqXbDzz+wCjgGO/Ek2VaQRSaMuDnukMUMyndPpZdInaua8TEKnvFgHrdeYTogSsI+sbpDlGspHT73hjgcO/4EyYf8JpC5Ccb8GvdIYqVlG4fyo5yz3YNH19uLx8gB0KIQnYmQV93NicXXSSl27f8wHjPIcccqjuIEH3gOt0BipGUbt+aY/cNMuxVQ2Q+TBSDMwj6BusOUWykdPuIxx8YAhzmHT9ztKzLFUXCDlyhO0SxkdLtOycoh8t0DhwtZ4QoIbGUyfQ/dXL4HzuZcFsn//5KDID1rRkCf+5kzK0dXPhwhETa3O99bAxlKP9VOzctts5Y3hzOcOwdYSbe1snja5KfXO/MByJs7cj07zf0RVcS9Mkgog9J6fYBjz9QDpzsHT9zkLI73LrziNxx2eDly72suKqc977t5bl1KZZsTvEvL8b4wVEu1n6/gmq34i/Lk/u9jx8uivEV/6fniL3/H0muOtLB0m96uWVJAoCnPkwyZbDB0IqcP2VHAyfl+kGLmZRu3wgAdtew8UfqDiJySylFudMaCCYzkEyDAl5en+a88VaRXn64g8c/3HfpPr4myUFVBhPqPn0qOgxFJAnxFNgMSGVMbmlIcP0MbZuAfVPXAxcjKd1e8vgDdmCOc9AYZSurkNPwlKB0xmTyHzsZ+LsOTh1t5+Aagyo32A2rjIdXGmxp/+L0QmfC5DdvJfj3mZ8t00smOXjiwxSn3hPmJ8e6uO3tBF87zIHHoe1V/tkEfQN0PXixsR/4KuIAxgLVZaOnjtEdROhhMxTvXVVOW8zk7AcjrNnVtXnX4KtxfnCU85OR8h4+t2LhJR4AWqMmC96K89iFHr75ZJTWmMmPjnZy9IicPnWdwGXAzbl80GIlpdt7M4C4o3bUJN1BhF5VbsWJ9Xb+vilNW8yaFrAbis3tGYZVfnGU2rAlzcOrk1z/Qoy2mImhwG1XfHe685Pr3Ph6nJ8e5+L+95McO9LGeeMdnPO3CIvm5fyp+02kdPuETC/0gscfKAOmueunlBlOd6XuPCL3msMZ2mLW1EE0afLCxynG1RmceJCNh1enALhrRZIzxzq+cNs3rvDSdG0FTddWcO1RTn5ynOszhdvYkmZze4aZ9XYiSauUlYLo/t+T60/jCPpmaHnkIiMj3d6ZANjdIydN1B1E6LGt0+TyxyOkM5Ax4YIJDs44xMH4OhsXPRzhZy/HmDLExv+bYpXukx8meWdrmhtOPPAil5++HOeXJ1nzvRdPcnDWA1EWvJXghpla31B7S9eDFwtlmvtfPyi+nMcf+CGGfUzd3OuukKViufXb2C82XFC1Wva3yK3dQB3BUM4XCxcTmV7oIY8/4AMmuEcd5pHCFSWiBpDd83pJSrfnJgDKNdh/sO4gQuTQyboDFDop3Z4LAGF79RBZKiZKiZRuL0np9oDHH3AB420VtUnDXSG7MIlSchxBn/PAVxP7I6XbM/WA4R51+EGyoZgoMR7gKN0hCpmUbs+MB0xnXb1MLYhSJFMMvSCl203ZU/JMB1ptFXJKHlGSpHR7QUq3+2qAwXbfYMNwuCt0hxFCg+kEfeW6QxQqKd3uGwmYzsFjhukOIoQmDuB43SEKlZRu940GMo6aoVK6opTJFEMPSel23zig3VZRO1R3ECE0ktOz95CUbjdkNywfBXTaPD4pXVHKDtUdoFBJ6XbPYMBw1I6qUjbZb0GUtCo5PXvPSOl2z1BA2auHyqlLhLCm2kQ3Sel2z8FA0l5eU6M7iBB5QKYYekBKt3tGAFHDWyWlK4SUbo9I6XbPECBqc1dU6w4iRB6QbU17QEq3izz+gBPwAXHD5ZWRrhDWgUKim6R0u64aMFFKKWdZle4wQuQBKd0ekNLtuhrAtFcOLFeGYdMdRog84CPok7Ngd5OUbtfVADajrKJMdxAh8oiMdrtJSrfraoG04ZbSFWIvI3QHKDRSul3nA5KGyyNHognxKdnetJukdLuuEkgZTo+MdIX4lEN3gEIjpdt1FUBSOd1SukJ8yq47QKGR0u26CiClHG6ZXhDiU1K63SSl23VeIKUMu7ycEuJTUrrdJKXbBdmTUZYDSd1ZhMgzMgjpJindrjMAU3cIIfKMjHS7SUpXFKSHjdM8yztqNqczZlp3lhInpdtN8g8mCtJS5/S6c5hOZbQtfnHysS3nOxY7R3s6BxlKKd3ZSox0SDfJSFcUtHZblet29xUjT7H9afCx4d+Gb28LbNgWc+zSnauEyJxuN8lvqW4zZV43T221jyj/tf2a8l8D49pXt16ReTQ0y7OmxufMyKYs/Uc6pJvkH6ybzHRKVjAUgA+c46uvZ3z19RmYEXprx+U8HTvOu2FgmR05uKVvyXRON0npdp0CMJPxmO4gonvecs0Y9BYzsCfjmdmdL2ydZ3shPcXbPNhhyEvjPrBTd4BCI3O6XRBpbDCBOGAzk7G47jyiZ1LKZTzpPmPoBY7fj5gcvd28oW32pjXhiq0ZU6aMemGL7gCFRka6XRcBbJlENKo7iOi9sK3CeYdt3og7mMfAyPbIZclHms9yveMZXhav052twGzVHaDQSOl2XRSwZ2KdEd1BRN/aaRvsucl29aibAH/Hh21fTz/W9pWyVVU1rrSclunApHS7SaYXuq4DsGei7VK6RazRMbbqp+759UeY91Rd0H5t8zOh0RsiSSX/5/uWAbbpDlFoZKTbdSFgaKqzpVN3EJEbS53T65YyHSOVMmeFX9o6z1iUmu7dPthhw6k7W55oJhhK6Q5RaKR0u64VcGYioRYzlYwpu0O2eCwRGWVXz7pnDX2WWZTFw8lzE09tusj+mjHO0zbEZqhSfrUoUws9UMo/MN3VQvbom0wisltzFqFJ1PA67nVfNOIM+/8Mmxa5NX5z2wkbNkTcO0p0AYSsXOgBKd2uayG7y1gm1tmqOYvIA7vtdWW/d3971AnGHYNO7Pxl+51tU5qaY/ZS+tmQkW4PSOl23W72lG60Q0a64jOaHKMrg+7r6qdxd/VZ7dfteiLk39CZVMU+/y8j3R6QOd2uayX7SyodbpXSFfv1nnNK7TVMqVWplHlS5LXtl6nnEkd5twxy2XDpztbHZKTbA1K6XdcOpAEj1bGrlF5Cih4ylV295Dp58EucjDMeS5+ZWLj5EtsrHOZtGWIzlE13vj7QqDtAIZLphS6KNDZkgB1AWWLnejneXHRLwnDbHnKfO/xsx38PPyL6h+SCtlM2rot4thfwG3Ap4G3dIQqRlG73bAPKMpG2aCYekdGu6JGQrcb9R/c3Rp5s/HnwseHfdvypbVrT9pijRXeublpBMCQHjfSAlG73rANra8B0uFXeRBC9tsU+ouKX7h/UH8VdA+a0/2T3w22HNrUnjHbdubpgse4AhUrmdLtnI9kVDKn2nVsdNcMmas4jisgq58Saf2ZiDekMx4fe2nEZT8dmeDfl6x7AUro9JKXbPVvJvjpI7tq0pax+iuY4oigpg9ddxw16neOwJ+OZMzoXbbnU9mJminfXELuRN8/Zv+sOUKjy5T+wUISwVjG44ts+3GaapqnkRIiiH6WUy3jc/dVhj/NVyqPtiQuTj2+8wPGmw+/pGKzxJJxbCIY2aHrsgidzut2Q3cy8EagwE9FkJtYhqxhEznTaKp1/cV82cpbtf4ccHf6PyH+3HbNhS9TZrCGKjHJ7QUq3+1YDXoBU246PNWcRJWqHfaj3Jvd3R81Qd9ad1vFvrfe3TWxqTRihHD28zOf2gpRu923G2keUxPbGtZqzCMFHjkOrf+z+Sf2UzL2+i9q/3/xc6KANkRT9uZxLRrq9IHO63bcBq3RtsY0rN5QfflpSGXY5waHIC0ucR9Ut4ShsyWTm9M4Xt84znk8f6d0xqK/2ADZNM6aUWt4X91WqVAEfEaONxx+4FjgYaKk55apL7L6Bft2ZhNifskw4eV7iye0X2V8zxnlDQwzVqz2A3yAYOr7PwpUgmV7ombeBcoBkyyaZYhB5LWp4Hfe4Lx4xx/7HYdPCt8ZuaTt+w4aIu6dvAj/Wp+FKkJRuz6wle5BEbNM/pHRFwWix13lucV816gTjjoEndvyi/a62KU274rYuHdJuWi+LH+7niEVPphd6wOMPKOAmrE0/ogPm/OA7NnfFQB1ZMrFOWp69lcSujQDUzr4G5XDRsugPmIkYdt9Aaudeh+HydOm2rmHjaH31r0Q/XoZz4EHUnvEjADpXvUIm0k7ltDNz982JnDkisWzXFeYT4RM96waUO8zyfV0nY5oNxs/bj8p1tmIjb6T1QKSxwfT4A0uBU4AtyR3r37eNOuxkHVl2v/S/uEdPpe7sn2Cmk5jJODse/FeqT/wG7pGT6Fz5PO0Nj1B1/Ne6dNtMPExi+zqGfuO/rUJubsJeNYTw+y8w8PwbNHyHIheWO6fWLmdqrUqlzFMir267TD2bDHi3DXLutQewodSDOjMWC5le6Ln3ABtAZN3S93W8YsjEw8Q2raL8sNMAUDYHhruc5O4tuEZY20K466cQ+eiLyyr3d1tQmJkUpmmSScZRho32pY9SccRclE1+Rxc7U9nVC65ThnzN+R8jJ8X/bJvfdvbmZe1VzRmTBDK10CfkWdRza4Ew4E61bg2lw60b7eU1I3MZINW2A5unkpZnbiGxcz2uwWOoPvlbOGtHEm1cgueQo4mseZNUx64u39ZweSg7+Ei23fl93KMOR7m8JLZ9RNWMi3P5rYk8EDc89gfc5w9/gPPxxdpfXPGbizfpzlQMZKTbQ5HGhjTwGlALkNi+9v1cZzAzaRLb11ExZTZDr7gV5XDRvuQhBsy+ho53n2HbndeQSURRxhd/t+7vtgC+wHkMveK/qDnpSkJv3Ivv2EvpWLGI5scX0Lb4gVx/myIPhFTl33RnKBZSur3zNtkphujahlWmmcnk8sHtFbXYKmpxDR0LgGfsDBI71uEYMIJBF97IkK//Hu/4E7BXD+7ybfeW2LEO0zRx1AwnsuZN6s6aT6p1O8ndspVwSTEzcUBKt49I6fbORqAZ8KbDrdFU244Pc/ngtvJq7JW1JFs2AxDbsAJH7UjS4TYATDNDaPEDVEz+Spdvu7e2N+6l6rh5kEmBmf19ohRmKt6P35XINyY82rRgTq72dSh6MqfbC9lVDC8DFwDh6MfvNDimzh2Xyww1p1zFrqdvwkynsFcNZsDsawn/4yU6li8EwHPIMXgnnQpAqqOFluduZdD5P9/vbT/53j76O87BY7BXDADAOXA0W/9yNY6B9TgHjs7ltyg0U8q4RXeGYiLrdHvJ4w/UAb8BNgHmgNnXfttWVvnF1/NCFCAznVq+4XdnTtWdo5jI9EIvRRobmoF3gYEA8U3/aNCbSIi+o2z23+rOUGykdPvG82RPWBn+4PX3M6lEWHMeIXrNzKR3AI/ozlFspHT7xkfAFqDSTCXSie1rl+kOJETvqVubFsxJ6U5RbKR0+0D2ND5PA9UA4Q9ee9vMpOWHVRQsM5OJKsO4XXeOYiSl23eWA1HAlW5v7kzs+Pht3YGE6DEzfWvTgjktumMUIyndPhJpbIgDzwCDADpXLnrTTKcSelMJ0X1mJh1WNscC3TmKlZRu33oNSACudOfuSHx74xLdgYToLjOVvLlpwZw23TmKlZRuH4o0NnQAT7JntLviucVmKhnTm0qIrjPTqZDhdP9Gd45iJqXb914FYoA7E+2Ix7eukdNVi4JhplMLmhbM6dSdo5hJ6faxSGNDBGtt4yCAjhWLlmSSsQ69qYQ4MDOV2Gk43XLIbz+T0u0fbwEdgMdMRJLRxoZFugMJcSBmOvndpgVzZDqsn0np9oNIY0MMeIjsocHhD15blWrf9bHeVELsXzrasWTjzRc8pDtHKZDS7T+LgSaym5x3vPfMM2Ymk9aaSIh9MDPpFGbmMt05SoWUbj/JnlniLqAcsCWbm1ri2z6UN9VE3klHQn/YdOsljbpzlAop3X4UaWxYD7wIDAXoWPbU65lEVNY/iryRSUR32Mtrrtedo5RI6fa/J7CWkHnMZCwVXvXKU7KHscgHpmmamVjnN5oWzJEjJ3NISrefZQ+YuJfsErLox+98nNy5XvZlENqlQjvu23zb15/RnaPUSOnmRgOwChgMEFr6yAuZeFg2ExHapCPtW5PNTVfqzlGKpHRzINLYkAH+CiigzExEkx3vPvOIrGYQOpjpVCq5e/P5Ox+5UdbkalDypauUMpVS9+71Z7tSqlkp9fQBbjfzQNfZW/a0PncBQwAV3/LBttjGlS/3OLgQPZTcvfmW7fdeJytpNCn50gXCwESlVFn2z6dinQWiP/w9exkG0LHsycWp9ua1/fRYQnxBqn3XyrbX75bVChpJ6VqeAeZkP78YuH/PXyilpiul/q6UelcptVgpNfbzN1ZKeZVSdyillmavd+a+HiR7hol7sA4R9gG0vXXfI5l4ZHdff0NCfF462tEa37J6dvbnUGgipWt5ALhIKeUGDsN642uPNcBxpmlOAf4N+NU+bv9T4GXTNKcDJwK/U0p59/VAkcaGTuA2rFP7ODORUKz97ccekA3PRX8yU4lErGn5Jc1P/Ka/XsWJLpLSBUzTXAnUY41yP7+Exgc8pJT6B3AzMGEfd3EaMF8p9R7W1o5uYOT+Hi/S2NCItYxsOGAkdqxrDq9+9VFZvyv6g2lmzOj6d3/R/MRvn9OdRUjp7u1J4Cb2mlrIuhF4xTTNicBcrEL9PAWca5rm5OxlpGmaHxzg8V7CKuiRAJGPFn8Y37zqld58A0LsS3zLmsc6Vy76pe4cwiKl+6k7gJ+bpvn+577u49M31r6+n9suAr6nlFIASqkpB3qw7Lza/wFrya7fbV/66OvJ1q2rux9diH1LtGxa2d7w8LzsskWRB6R0s0zT3Gya5q37+KvfAr9WSr0L2Pdz8xsBB7BSKbUq++cDyp7M8jYgDlQBtL1+96OpjpambsYX4guSbds3dr737OmRxoao7iziU0rmEfXz+AOjsd6M2wVElcvrrDnpysttHt9QzdFEgUq1N+9of+eJWe1LH1uhO4v4LBnp5oFIY8PHWCPeQYDLjIcTba/ffW861tmsOZooQOlw6+72ZU/Ok8LNT1K6eSLS2LAM+AvWgROOdLg1Gnrz/+6RrSBFd6SjHe3ty57+VnvDoy/qziL2TUo3j0QaG97AWko2ArCnQjs6QosfuFtObCm6IhMPhzveXXhtsnn9o7qziP2T0s0/LwCPYi0lM5Itm1pDb953RyYeadWcS+SxdLQ9FFr66HWJbR/dKUec5Td5Iy0PefwBhXWgxunABiBtq6wrrzp23tdsZRUD9aYT+SbduXt3aMnDwVRo+x9kaVj+k9LNUx5/wAAuBL4CbARShsfnrj7+8ktt3qrhetOJfJFq37mzbfGD/5oJt/4le14+keekdPNYdsQ7FzgP2AwklNPjqJ759YvsFbWj9aYTuiV3b9kS+vuD/5KJdd4vI9zCIaWb57LFezJwGdaRcXFlc9h8x82b6xww4nC96YQu8e1r17UvffSHZjL2lMzhFhYp3QLh8QeOAb4N7AAiABVT5x7tHjX51D2HH4viZ5qmGV27dFnnykXXAa9J4RYeKd0C4vEHpgBXY5XuboCyg6cfXD7x5POU3bGvjXhEETHTyXjHe4tejzUt/9dIY0PDgW8h8pGUboHx+AMjgWuACmArgKN2VE1l4NyLbBl+/+wAAAZuSURBVO7yOq3hRL9JR9t3h5Y8tDC1e8sNkcYGOdtIAZPSLUAef8AHXAWMw1rZkDHc5U7fMRed6ageOl5vOtHXEs1NH4caHnnIjIdvijQ27NKdR/SOlG6B8vgDDuACYBbZN9gAyiedMrns4OlfUTa7U2c+0XtmOhkPr37t7chHi+8B7o40NsjZe4uAlG4By65sOB64HOsEmy0AjgEjqiunnXWOzVst63kLVKpj15b2hoffSoV2/hl4Ud4wKx5SukUgO8/7bWAo1nreNMpQldPPPt41bPwJsrqhcJhmJhP9ePnyzhXPvoJp/jG7A50oIlK6RcLjD7iAc7AOHd6FdcZhXCMmDiufdMpcW1nlIJ35xIGlw207Ot5d+HZix7qHgb/J5uPFSUq3yHj8gQlYo94yrNUNJspQFVNmT3ePPOxEZbO79CYUn2emk7HI2reXhVe9tALT/F9gpUwnFC8p3SKUXd0wDwhgjXrbAWyVA8srp86d5agZNlFnPvGpRPOGVe3vPLE6E2lbDNwVaWyQ3eSKnJRukcq+yTYR62SaNVij3iRA2eipB3nHnTDbcJfX6ktY2tLRjubOlYvejm9e3QjcBbwno9vSIKVb5Dz+gBtrWdmZQALYDoAyVPnEkw531085wXCWVWmMWFIy8UhrZG3D8siHb27CNJ8GnpG529IipVsiPP7AEOBSYBLQClinAbLZjfJJpx7hHjnpeMPhrtAYsahlErH26PrlDeHVr2wnk14N3BNpbNiiO5fIPSndEpKdcpgEXIS1vKyF7CoH5XDbyw87bZp7+Phjld3p0RizqGSS8XBs48qlne+/uJl0chvwINZUgmzFWKKkdEuQxx+wAZOxNkkfCDRjHVyBcrjt3vEzJ7tHTDjKcHkHaIxZ0NLR9u2xDSvfDa95YxfpZDPwN2BZpLEhpTub0EtKt4R5/AE7MA3rcOJq9hr5AngOOfoQ96jJ020VtQfL8RUHZpqmmWrbvia6tmFlbOPKGBACHgaWRBobkprjiTwhpSvw+ANOrPI9E6gDOrG2jjTB2sXMM/aYaY4BIycZDpdXX9L8lEnGOpK7Nr4fXv3qulTb9jTWMr2ngIZIY0NcczyRZ6R0xSey0w7jgdnAoUAK2El2qRnKUGWjjxztGjFhkqNqyLhS3lTHTCfjydatq2Mb318Va3o3hmnagVXAs8AaOV+Z2B8pXbFPHn9gGHACMBNwYM357gYyYM39esYExjqHHjrJXll7sDJsdm1hc8TMpJOp9p3r4lvWvB9d27DLTCXKsH4xvQq8KqsRRFdI6Yov5fEHyrBGv8djrXwA6wi3tj3XUQ633T3qsFHOQWPGOKqGjDHc3qI56CId62xOtW5bm9ixdm2saUWbmU6UZ//qA6yyXR1pbAjrSygKjZSu6LLs4cWTgJOA+uyXO7HeMPrk5bS9eqjPPXLSGMeAEQfZvNXDCungi0w80poOt25JtmxaH9u4cl2qbbsNKAcU1obxrwAr5HBd0VNSuqJHPP7AQGAs1htw47FKycQ68OIzIz9beY3HOdg/1FEzfJi9snao4akalg9vyGWS8c50uG1LuqN5a3L35i3xrR9tzUTaFNZKDiN7tTXAUuBDYIccqit6S0pX9Fp2W8mDgAnAdKwVEGCVcBhrOuIz61MNj8/tqBleY6+sq7F5q6sNj6/GcJfXGE5PlbI7ypRhc/Q2l5lJJc1UMmImoqFMPNKWjnW0pTt3706FdrYkWza1ZCJtSaxzze2ZMlBYy+YasN4UWy9naxB9TUpX9KnsUW9VWEe8jcI6j9sYYM9KBwXEgGj2ss+DBZTdaTM8vjJbWWWZ4S53Gy5vmbI7HLDvBcNmKp7IxMLRTKwzmo62RzORUMxMJ/dMeRhYW13uueyRBNZhzc82YW0K1CqjWdGfpHRFv/P4AwYwABiGdQTcCKxSHoJVgmmsMgawZf+cxCrkJNaKif39oNqwVlfYsxdb9rp7rq+yt9+OdVaNjcA2rIJtlsNxRa5J6QptsqNiD9YcalX2czdQCfiyHyuyX9sXhTVa7sCawthz2TOKDmGtsuiQ0avIF1K6QgiRQ8aBryKEEKKvSOkKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQOSekKIUQO/X8yAWySrGBvFQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = sns.countplot(x = 'target', data = data, hue = 'sex')\n",
        "fig.set_xticklabels(labels=[\"Doesn't have heart disease\", 'Has heart disease'], rotation=0)\n",
        "plt.legend(['Female', 'Male'])\n",
        "plt.title(\"Heart Disease Frequency for Sex\");"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "Jfioa66AHAQ0",
        "outputId": "7adf1d66-6ca5-4065-cec8-bef1634c7f3c"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = data.cp.value_counts().plot(kind = 'bar', color = ['salmon', 'lightskyblue', 'springgreen', 'khaki'])\n",
        "fig.set_xticklabels(labels=['pain type 0', 'pain type 1', 'pain type 2', 'pain type 3'], rotation=0)\n",
        "\n",
        "plt.title('Chest pain type vs count');"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "id": "NZg7Lf8gHMY_",
        "outputId": "c3ee471f-c7db-4cd6-d495-9f3dc461a7c3"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAEICAYAAACktLTqAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAVcklEQVR4nO3de7ClVX3m8e8DDYJiAOEMg3RLm4AX4pSoDUJpUgleBggTGAMKIiCD6YmDMxq1EsykFDM3TUpNrCgOEQOoRC4aoRwzhkI0oyVIcxG5GToE7G5ujXKNo9x+88e7erI5ntPnnD779OlefD9Vu/b7rnftd629+vSz373ed++dqkKS1JdtFrsDkqTxM9wlqUOGuyR1yHCXpA4Z7pLUIcNdkjpkuGtKSU5P8rnF7sdcJDk+yd8udj+kLYHh/jSW5M1JViV5JMldSf4myasXsL3lSSrJkoXYf1V9vqpevymP3RpfzBZbkrcm+dZi90NTM9yfppK8G/hT4L8DewDPAz4JHLmY/ZI0JlXl7Wl2A3YGHgGO2Uid04ELgHOBh4EbgRUj258LfBFYD/wj8J9Gth0IrAIeAu4BPtrKfwhUa/sR4OBp2r0IOL+1ew3w0pHtpwH/0LbdBPzbkW1vBb41sl7A7wC3Ag8AnwAyRZuHAo8Cj7V+fQ84Brh6Ur13Axe35bOBTwGXtr58E9h7pO6L2rYfAz8A3jjNOL8JWDWp7HeBS9ry4e15PgysA967kX+z3wZuHhmbl7fyFwPfaGNwI/CbI4/5BvC2uY5h2+dPgSfamD2w2H/X3ib9PSx2B7wtwj/6EGaPA0s2Uuf09p/3cGBb4H8AV7Rt2wBXA+8Htgd+EbgN+Ndt+3eAE9ryTsBBbXl5C4uZ2n0MOBrYDngvw4vHdm37MQwvLNu0YPwnYM+2bapg+gqwC8M7k/XAoRtp93Mj689owfzikbJrgd9qy2e3EP3VVvfPNrQNPAtYA5wMLAFeBtwH7DdFu89s+9l3pOwq4Ni2fBfwK2151w2BPcV+jmEI/wNa+O4D7N3GcDXwB+3f6pDW3gvb477BzOE+5RhOrutty7o5LfP0tBtwX1U9PkO9b1XVV6vqCeCzwEtb+QHARFX9UVU9WlW3AX8BHNu2Pwbsk2T3qnqkqq6YY/+urqqLquox4KPADsBBAFV1YVXdWVVPVtX5DEeUB25kXx+qqgeq6ofA5cD+s+lAVf2M4d3DWwCS/DLDi9NXRqr9r6r6u1b3PwMHJ1kGHAHcXlV/WVWPV9W1DO9yjpminZ8AFwPHtXb2ZTjqv6RVeQzYL8kvVNX9VXXNNF1+G/DHVXVVDVZX1R0M47ZTG4dHq+rr7TkcN5txaDZpDLW4DPenpx8Bu8/ixObdI8s/AXZoj9kbeG6SBzbcGI4M92h1TwFeANyS5KokR8yxf2s2LFTVk8BahqN1kpyY5LqRdl8C7D6H57DTHPpxDvDmJAFOAC5oQT5VPx9hONJ/LsP4vHLS+BwP/Mtp2jmPfw7bNwNfbqEP8FsM757uSPLNJAdPs49lDNNVkz0XWNPGcYM7gL2m2c9U5jOGWiQLctWCtnjfAX4GHMUwvz1Xa4B/rKp9p9pYVbcCxyXZBngDcFGS3Rje4s/Gsg0LbR9LgTuT7M3wDuE1wHeq6okk1zFMQ8zXz/Wtqq5I8ijwKwyh++aN9HMn4DnAnQzj882qet0s274UmEiyP0PI/+5IH64CjkyyHfAOhvMgy6bYxxrgl6YovxNYlmSbkYB/HvD3bfmfGKaGNpjuBWgqfqXsFswj96ehqnqQYb78E0mOSvLMJNslOSzJH89iF98FHk7y+0l2TLJtkpckOQAgyVuSTLQweaA95kmG+donGeboN+YVSd7Q3iW8i+GF6AqGuexq+yHJyQxH7uNwD7C8vZiMOhf4c+Cxqpp82d/hSV6dZHvgvzCck1jDMO3xgiQntHHdLskBSV48VcNt+ulC4E8YXiAubc9v+3bt/s6tzkMM4zeVTwPvTfKKDPZpL4ZXMhxt/17rx68B/wb4QnvcdcAb2t/APgzvumbrHmBpe/7awhjuT1NV9RGGqz/+kCEs1zAcGX55Fo99gmFeeX+Gk533MYTLzq3KocCNSR5hONF4bFX93zbV8N+Ab7fpioOmaeJihpOl9zNMh7yhqh6rqpuAjzC887gH+FfAt+f63KdxYbv/UZLRee3PMryATHUN/HnABximY15Bm5+vqoeB1zOcg7iTYVrjwwwnXqdzHvBa4MJJ50JOAG5P8hDDVSvHT/XgqrqQYWzPYzhh+mXgOVX1KEOYH8bw7/RJ4MSquqU99GMMVwrdwzAN9fmN9HGyrzNcfXN3kvvm8DhtBqnynZW2HElOB/apqrcsdl8AkuwI3MtwlcqtI+VnA2ur6g8Xq2/SxnjkLm3c24GrRoNd2hp4QlWaRpLbGU7WHrXIXZHmzGkZSeqQ0zKS1KEtYlpm9913r+XLly92NyRpq3L11VffV1UTU23bIsJ9+fLlrFq1arG7IUlblSR3TLfNaRlJ6pDhLkkdMtwlqUOGuyR1aFbhnuT2JN9vX7W6qpU9J8mlSW5t97u28iT5eJLVSa5P8vKFfAKSpJ83lyP3X6+q/atqRVs/Dbisfe3rZW0dhi8o2rfdVgJnjKuzkqTZmc+0zJEM3yJHuz9qpPzc9mswVwC7JNlzHu1IkuZotuFewN8muTrJyla2R1Xd1Zbv5p9/hWcvRn6hhuFXdH7uV1+SrEyyKsmq9evXb0LXJUnTme2HmF5dVeuS/Avg0iS3jG6sqkoypy+pqaozgTMBVqxY4RfcSNIYzSrcq2pdu783yV8z/CDxPUn2rKq72rTLva36Op76M2BLW9lm9dgH37O5m9wk233gI4vdBUkdmnFaJsmzkjx7wzLDL8zcwPDr7Ce1aicx/HoOrfzEdtXMQcCDI9M3kqTNYDZH7nsAfz38ADxLgPOq6n8nuQq4IMkpDL+m/sZW/6sMv9a+muG3G08ee68lSRs1Y7hX1W3AS6co/xHDr9BPLi/g1LH0TpK0SfyEqiR1yHCXpA4Z7pLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOGe6S1CHDXZI6ZLhLUocMd0nqkOEuSR0y3CWpQ4a7JHXIcJekDhnuktQhw12SOmS4S1KHDHdJ6pDhLkkdMtwlqUOGuyR1yHCXpA4Z7pLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdWjW4Z5k2yTXJvlKW39+kiuTrE5yfpLtW/kz2vrqtn35wnRdkjSduRy5vxO4eWT9w8DHqmof4H7glFZ+CnB/K/9YqydJ2oxmFe5JlgK/AXy6rQc4BLioVTkHOKotH9nWadtf0+pLkjaT2R65/ynwe8CTbX034IGqerytrwX2ast7AWsA2vYHW/2nSLIyyaokq9avX7+J3ZckTWXGcE9yBHBvVV09zoar6syqWlFVKyYmJsa5a0l62lsyizqvAn4zyeHADsAvAH8G7JJkSTs6Xwqsa/XXAcuAtUmWADsDPxp7zyVJ05rxyL2q3ldVS6tqOXAs8PWqOh64HDi6VTsJuLgtX9LWadu/XlU11l5LkjZqPte5/z7w7iSrGebUz2rlZwG7tfJ3A6fNr4uSpLmazbTM/1dV3wC+0ZZvAw6cos5PgWPG0DdJ0ibyE6qS1CHDXZI6ZLhLUocMd0nqkOEuSR0y3CWpQ4a7JHXIcJekDhnuktQhw12SOmS4S1KHDHdJ6pDhLkkdMtwlqUOGuyR1yHCXpA4Z7pLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOGe6S1CHDXZI6ZLhLUocMd0nqkOEuSR0y3CWpQ4a7JHXIcJekDhnuktShGcM9yQ5Jvpvke0luTPLBVv78JFcmWZ3k/CTbt/JntPXVbfvyhX0KkqTJZnPk/jPgkKp6KbA/cGiSg4APAx+rqn2A+4FTWv1TgPtb+cdaPUnSZjRjuNfgkba6XbsVcAhwUSs/BziqLR/Z1mnbX5MkY+uxJGlGs5pzT7JtkuuAe4FLgX8AHqiqx1uVtcBebXkvYA1A2/4gsNsU+1yZZFWSVevXr5/fs5AkPcWswr2qnqiq/YGlwIHAi+bbcFWdWVUrqmrFxMTEfHcnSRoxp6tlquoB4HLgYGCXJEvapqXAura8DlgG0LbvDPxoLL2VJM3KbK6WmUiyS1veEXgdcDNDyB/dqp0EXNyWL2nrtO1fr6oaZ6clSRu3ZOYq7Amck2RbhheDC6rqK0luAr6Q5L8C1wJntfpnAZ9Nshr4MXDsAvRbkrQRM4Z7VV0PvGyK8tsY5t8nl/8UOGYsvZMkbZLZHLlLfOjaxxa7C7Ny2su2W+wuSFsEv35AkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOGe6S1CHDXZI6ZLhLUocMd0nqkOEuSR0y3CWpQ4a7JHXIcJekDhnuktQhw12SOmS4S1KHDHdJ6pDhLkkdMtwlqUOGuyR1yHCXpA4Z7pLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOzRjuSZYluTzJTUluTPLOVv6cJJcmubXd79rKk+TjSVYnuT7Jyxf6SUiSnmo2R+6PA++pqv2Ag4BTk+wHnAZcVlX7Ape1dYDDgH3bbSVwxth7LUnaqBnDvaruqqpr2vLDwM3AXsCRwDmt2jnAUW35SODcGlwB7JJkz7H3XJI0rTnNuSdZDrwMuBLYo6ruapvuBvZoy3sBa0YetraVTd7XyiSrkqxav379HLstSdqYWYd7kp2ALwLvqqqHRrdVVQE1l4ar6syqWlFVKyYmJubyUEnSDGYV7km2Ywj2z1fVl1rxPRumW9r9va18HbBs5OFLW5kkaTOZzdUyAc4Cbq6qj45sugQ4qS2fBFw8Un5iu2rmIODBkekbSdJmsGQWdV4FnAB8P8l1rewPgA8BFyQ5BbgDeGPb9lXgcGA18BPg5LH2WJI0oxnDvaq+BWSaza+Zon4Bp86zX5KkefATqpLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOzeYTqpLGKJy+2F2YldpK+qmpeeQuSR0y3CWpQ4a7JHXIcJekDhnuktQhw12SOmS4S1KHDHdJ6pDhLkkdMtwlqUOGuyR1yHCXpA4Z7pLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOGe6S1CHDXZI6ZLhLUocMd0nq0IzhnuQzSe5NcsNI2XOSXJrk1na/aytPko8nWZ3k+iQvX8jOS5KmNpsj97OBQyeVnQZcVlX7Ape1dYDDgH3bbSVwxni6KUmaixnDvar+DvjxpOIjgXPa8jnAUSPl59bgCmCXJHuOq7OSpNnZ1Dn3ParqrrZ8N7BHW94LWDNSb20r+zlJViZZlWTV+vXrN7EbkqSpzPuEalUVUJvwuDOrakVVrZiYmJhvNyRJIzY13O/ZMN3S7u9t5euAZSP1lrYySdJmtKnhfglwUls+Cbh4pPzEdtXMQcCDI9M3kqTNZMlMFZL8FfBrwO5J1gIfAD4EXJDkFOAO4I2t+leBw4HVwE+Akxegz5KkGcwY7lV13DSbXjNF3QJOnW+nJEnz4ydUJalDhrskdchwl6QOGe6S1KEZT6hK0pbswbs+sthdmJWd93zPZm3PI3dJ6pDhLkkdMtwlqUOGuyR1yHCXpA4Z7pLUIcNdkjpkuEtShwx3SeqQ4S5JHTLcJalDhrskdchwl6QOGe6S1CHDXZI6ZLhLUocMd0nqkOEuSR0y3CWpQ4a7JHXIcJekDhnuktQhw12SOmS4S1KHDHdJ6pDhLkkdMtwlqUOGuyR1aEHCPcmhSX6QZHWS0xaiDUnS9MYe7km2BT4BHAbsBxyXZL9xtyNJmt5CHLkfCKyuqtuq6lHgC8CRC9COJGkaqarx7jA5Gji0qt7W1k8AXllV75hUbyWwsq2+EPjBWDuyMHYH7lvsTnTE8Rwfx3K8tpbx3LuqJqbasGRz92SDqjoTOHOx2t8USVZV1YrF7kcvHM/xcSzHq4fxXIhpmXXAspH1pa1MkrSZLES4XwXsm+T5SbYHjgUuWYB2JEnTGPu0TFU9nuQdwNeAbYHPVNWN425nkWxV00hbAcdzfBzL8drqx3PsJ1QlSYvPT6hKUocMd0nq0NMu3JP8UZLXzqH+/kkOX8g+tXa2uq9s2ILH8jNJ7k1yw0K3NU5b4ngmWZbk8iQ3JbkxyTsXsr1x2kLHc4ck303yvTaeH1ywtpxz37gkbwVWTP4Q1pjb2Bb4e+B1wFqGK46Oq6qbFqrNxbA5xrK186vAI8C5VfWShWxrMW2mv809gT2r6pokzwauBo7q7W8TNtt4BnhWVT2SZDvgW8A7q+qKsTdWVVvtDVgO3AJ8HrgZuAh4Ztv2foaQvIHhzPeGF7KzgaPb8u3AB4FrgO8DL5q0/+2BHwLrgeuANwG3AhNt+zbAamCi7fdTwCqGoD6i1dkW+JPWl+uBfz/F8zgY+NrI+vuA9zmWcx/LSc/nBv82xzOeI+1eDLzO8Zz/eALPbP155UKMWQ/TMi8EPllVLwYeAv5DK//zqjqghiO3HYEjpnn8fVX1cuAM4L2jG2r4bpz3A+dX1f5VdT7wOeD4VuW1wPeqan1bX87w3Tq/AXwqyQ7AKcCDVXUAcADw20meP6kPewFrRtbXtrLNrYex3JJ0NZ5JlgMvA66c3dMfuy7GM8m2Sa4D7gUuraoFGc8ewn1NVX27LX8OeHVb/vUkVyb5PnAI8MvTPP5L7f5qhn+wmXwGOLEt/zvgL0e2XVBVT1bVrcBtwIuA1wMntn/MK4HdgH1n0c5icCzHq5vxTLIT8EXgXVX10Cz6shC6GM+qeqKq9mf49P6BSRZk6nDRvltmjCafNKj2KvpJhvmzNUlOB3aY5vE/a/dPMIvxaPu7J8khDK/cx49unqJvAf5jVX1tI7vdUr6yoYex3JJ0MZ5tbviLwOer6ksbq7vAuhjPkf0/kORy4FCGKaWx6uHI/XlJDm7Lb2Y4QbHhH/e+dsRx9Dz2/zDw7Elln2Y4criwqp4YKT8myTZJfgn4RYZvuvwa8Pb2H4QkL0jyrEn721K+sqGHsdySbPXj2U4AngXcXFUfnUdfx6GH8ZxIsktb3pHhIopb5tHnafUQ7j8ATk1yM7ArcEZVPQD8BcOr4dcYwnNTXQ7sl+S6JG9qZZcAO/HUt2kwnJD5LvA3wO9U1U8Z/jhuAq5pl+b9TyYdNVTV48CGr2y4meEt32J8ZcNWP5YASf4K+A7wwiRrk5wyjz7PRw/j+SrgBOCQ1s51C3254Eb0MJ57Apcnub719dKq+so8+jy9hThLu7luLNIVEcAK4P9MKjubdmZ+a7w5lo7nlnxzPOd+62HOfbPK8AGjt/PU+TdtAsdyvBzP8drax9MPMUlSh3qYc5ckTWK4S1KHDHdJ6pDhLkkdMtwlqUP/D31PjYTw4JjwAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = sns.countplot(x = 'cp', data = data, hue = 'target')\n",
        "fig.set_xticklabels(labels=['pain type 0', 'pain type 1', 'pain type 2', 'pain type 3'], rotation=0)\n",
        "plt.legend(['No disease', 'disease']);"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 279
        },
        "id": "z47zQK4CHXRs",
        "outputId": "1dbd4fc5-ca0d-4d7a-f3a0-64a6d1081656"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,6))\n",
        "\n",
        "#plotting the values for people who have heart disease\n",
        "plt.scatter(data.age[data.target==1], \n",
        "            data.thalach[data.target==1], \n",
        "            c=\"tomato\")\n",
        "\n",
        "#plotting the values for people who doesn't have heart disease\n",
        "plt.scatter(data.age[data.target==0], \n",
        "            data.thalach[data.target==0], \n",
        "            c=\"lightgreen\")\n",
        "\n",
        "# Addind info\n",
        "plt.title(\"Heart Disease w.r.t Age and Max Heart Rate\")\n",
        "plt.xlabel(\"Age\")\n",
        "plt.legend([\"Disease\", \"No Disease\"])\n",
        "plt.ylabel(\"Max Heart Rate\");"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 404
        },
        "id": "mlhiUEMbHnhC",
        "outputId": "eb9930bf-7dbb-48a1-e982-1420b560b494"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x432 with 1 Axes>"
            ],
            "image/png": "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sZnZH4Gr3P2nofsiIo1DGTIRaWhm9lEz+7t4yHIq0UT1JNkbEZGKyWS5CxGRHNkRuJGoZMgLwDHuvjBsl0Sk0WjIUkRERCQwDVmKiIiIBKaATERERCSwXM8hGzNmjG+zzTahuyEiIiLSr0ceeeR1dx9b6rFcB2TbbLMNc+bMCd0NERERkX6ZWdkl0TRkKSIiIhKYAjIRERGRwBSQiYiIiASW6zlkIiIiksyqVavo7Ozk3XffDd2VujdixAiam5sZPnx44p9RQCYiItIAOjs72Xjjjdlmm20ws9DdqVvuzpIlS+js7GTbbbdN/HMashQREWkA7777LptuuqmCsYyZGZtuumnqTKQCMhERkQahYKw6BnKcFZCJiIhIVQwdOpSWlhZ23nlnPvzhD3PppZeyZs0aAObMmcNpp50WuIfhaA6ZiIiIVMXIkSN5/PHHAVi0aBGf+9znePPNN/nud79La2srra2tgXsYjjJkfTl/Gpx82Nrb+dNC90hERKQ6Zt8DZ7fDyZ+Ivs6+p6Kb32yzzZgxYwZXXnkl7s69997LkUceCcB9991HS0sLLS0tTJ48meXLlwPwwx/+kClTpjBp0iS+/e1v92zrU5/6FLvvvjs777wzM2bMAGD16tWccMIJ7LLLLuy6665Mnz4dgOeff57DDjuM3XffnY985CPMmzevoq9roJQhK+f8afDqy+u2vfpy1H7BjDB9EhERqYbZ98Csy+C9ldH9pYui+wB7HVSx3Wy33XasXr2aRYsWrdN+ySWX8O///u/su+++rFixghEjRnDnnXcyf/58Hn74YdydT37yk9x///3sv//+zJw5k9GjR/POO+8wZcoU2traePHFF1mwYAFPPfUUAG+88QYA06ZN46qrrmL77bfnj3/8I1/72te4557KBpsDoYCsnOJgrL92ERGRenHLtWuDsW7vrYzaKxiQlbPvvvty5plncvzxx3P00UfT3NzMnXfeyZ133snkyZMBWLFiBfPnz2f//ffn8ssv59ZbbwXglVdeYf78+ey444688MILnHrqqRxxxBEccsghrFixggcffJBPf/rTPftauXJlyT5UmwIyERERWdfSxenaB+iFF15g6NChbLbZZsydO7en/dxzz+WII47g9ttvZ9999+WOO+7A3TnvvPP48pe/vM427r33Xu666y4eeughNthgAw444ADeffddmpqaeOKJJ7jjjju46qqruPHGG/nxj3/MJpts0jOPrZZoDpmIiIisa/TYdO0DsHjxYr7yla/w9a9/vVeZiOeff55dd92Vc845hylTpjBv3jwOPfRQZs6cyYoVKwBYsGABixYtYtmyZTQ1NbHBBhswb948Zs+eDcDrr7/OmjVraGtr48ILL+TRRx/lAx/4ANtuuy033XQTEBVxfeKJJyr2mgYjswyZmW0FzAI2BxyY4e6Xmdlo4AZgG+BF4DPu3mXR2bgMOBx4GzjB3R/Nqn/92nJ86eHJLcdXvy8iIiLVdPQJ684hA1hv/ah9EN555x1aWlpYtWoVw4YN4wtf+AJnnnlmr+f9+Mc/5ve//z1Dhgxh55135hOf+ATrr78+c+fOZe+99wZgo4024rrrruOwww7jqquuYsKECey4447stddeQBSwnXjiiT1lNb7//e8DcP311/PVr36VCy+8kFWrVnHsscfy4Q9/eFCvqxLM3bPZsNkWwBbu/qiZbQw8AnwKOAFY6u4Xm9m5QJO7n2NmhwOnEgVkewKXufuefe2jtbXV58yZk0n/gd4T+7ccrwn9IiKSS3PnzmXChAnJf2D2PdGcsaWLo8zY0SdUZf5YvSh1vM3sEXcvWdsjswyZuy8EFsbfLzezucA44CjggPhpPwPuBc6J22d5FCHONrNNzGyLeDthKPgSEZFGtddBCsCqqCpzyMxsG2Ay8Edg84Ig6zWiIU2IgrVXCn6sM24r3tY0M5tjZnMWL67s5EIRERGREDIPyMxsI6AD+Ia7v1n4WJwNSzVm6u4z3L3V3VvHjq3c5EIRERGRUDINyMxsOFEwdr273xI3/y2eX9Y9z6y7GtwCYKuCH2+O20RERETqWmYBWXzV5DXAXHf/UcFDtwFT4++nAv9d0N5ukb2AZUHnj4mIiIhUSZaFYfcFvgA8aWbdFdi+BVwM3GhmJwEvAZ+JH7ud6ArL54jKXpyYYd9EREREakZmGTJ3/4O7m7tPcveW+Ha7uy9x94PdfXt3/5i7L42f7+5+irt/0N13dfcM61mIiIhItZkZZ511Vs/9Sy65hO985zuJf/7aa69l7NixTJ48me23355DDz2UBx98sOfx888/n7vuuquSXa4aVeoXERGRqlh//fW55ZZbeP311we8jc9+9rM89thjzJ8/n3PPPZejjz66Z9mlCy64gI997GOV6m5VKSATERGRXuatnMfMZTO5rOsyZi6bybyV8wa9zWHDhjFt2jSmT5/e67EXX3yRgw46iEmTJnHwwQfz8sslVsspcuCBBzJt2jRmzIjqhp5wwgncfPPNQLQe5sSJE5k0aRLf/OY3gWi5pra2NqZMmcKUKVN44IEHAHj44YfZe++9mTx5Mvvssw9/+ctfAHj66afZY489aGlpYdKkScyfPx+A6667rqf9y1/+MqtXrx78sRn0FkREGlDHsg4613T23G8e0kzbqLaAPRKpnHkr53H323fzPu8DsHzNcu5++24Adlp/p0Ft+5RTTmHSpEmcffbZ67SfeuqpTJ06lalTpzJz5kxOO+00fvWrX/W7vd12242f/OQn67QtWbKEW2+9lXnz5mFmvPHGGwCcfvrpnHHGGey33368/PLLHHroocydO5eddtqJ//u//2PYsGHcddddfOtb36Kjo4OrrrqK008/neOPP5733nuP1atXM3fuXG644QYeeOABhg8fzte+9jWuv/562tvbB3VcFJCJiKRUHIwBdK7ppGNZh4IyqQsPvvtgTzDW7X3e58F3Hxx0QPaBD3yA9vZ2Lr/8ckaOHNnT/tBDD3HLLVGFrC984Qu9ArZySi0BOWrUKEaMGMFJJ53EkUceyZFHHgnAXXfdxTPPPNPzvDfffJMVK1awbNkypk6dyvz58zEzVq1aBcDee+/NRRddRGdnJ0cffTTbb789d999N4888ghTpkwBovU5N9tss4EdjAIKyEREUioOxvprF8mb5WuWp2pP6xvf+Aa77bYbJ544+IIKjz32WK81I4cNG8bDDz/M3Xffzc0338yVV17JPffcw5o1a5g9ezYjRoxY5/lf//rXOfDAA7n11lt58cUXOeCAAwD43Oc+x5577slvfvMbDj/8cH7yk5/g7kydOrVnsfJK0RwykcG49Fw4+bC1t0vPDd0jEZFB23jIxqna0xo9ejSf+cxnuOaaa3ra9tlnH375y18CcP311/ORj3yk3+3cd999zJgxgy996UvrtHdnvQ4//HCmT5/OE088AcAhhxzCFVdc0fO8xx+PqnItW7aMceOi1RqvvfbansdfeOEFtttuO0477TSOOuoo/vznP3PwwQdz8803s2hRVNd+6dKlvPTSSwM4CutSQCYyUJeeC3MfX7dt7uMKykQk9/YZsQ/DigbRhjGMfUbs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IiIigSkgExHJEc31EqlPCshERHJEc71E6pPmkImI5IyCL5H6owyZiIiISGAKyEREREQCU0AmIiIiEpgCMhEREZHAFJCJiIiIBKaATERERCQwBWQiIiIigSkgExEREQlMAZmIiIhIYArIRERERAILEpCZ2Rlm9rSZPWVmvzCzEWa2rZn90cyeM7MbzGy9EH0TERERqbaqB2RmNg44DWh1912AocCxwA+A6e7+IaALOKnafRMREREJIdSQ5TBgpJkNAzYAFgIHATfHj/8M+FSgvomIiIhUVdUDMndfAFwCvEwUiC0DHgHecPf346d1AuOq3TcRERGREEIMWTYBRwHbAlsCGwKHpfj5aWY2x8zmLF68OKNeioiIiFRPiCHLjwF/dffF7r4KuAXYF9gkHsIEaAYWlPphd5/h7q3u3jp27Njq9FhEREQkQyECspeBvcxsAzMz4GDggBzAMwAABm9JREFUGeD3wDHxc6YC/x2gbyIiIiJVF2IO2R+JJu8/CjwZ92EGcA5wppk9B2wKXFPtvomIiIiEMKz/p1Seu38b+HZR8wvAHgG6IyIiIhKUKvWLiIiIBKaATERERCQwBWQiIiIigSkgExEREQlMAZmIiIhIYArIRERERAJTQCYiIiISmAIyERERkcAUkImIiIgEpoBMREREJDAFZCIiIiKBKSATERERCSzI4uIiIiL1blbXLLro6rnfRBPtTe0BeyS1TBkyERGRCisOxgC66GJW16xAPZJap4BMRESkwoqDsf7aRRSQiYiIiASmgExEREQkMAVkIiIiFdZEU6p2EQVkIiIiFdbe1N4r+NJVltIXlb0QERHJgIIvSUMZMhEREZHAFJCJiIiIBKaATERERCQwBWQiIiIigSkgExEREQlMAZmIiIhIYArIRERERAJTQCYiIiISmAIyERERkcAUkImIiIgEZu4eug8DZmaLgZdC96PAGOD10J2Qfuk81T6do3zQecoHnafasbW7jy31QK4DslpjZnPcvTV0P6RvOk+1T+coH3Se8kHnKR80ZCkiIiISmAIyERERkcAUkFXWjNAdkER0nmqfzlE+6Dzlg85TDmgOmYiIiEhgypCJiIiIBKaAbIDMbISZPWxmT5jZ02b23bh9WzP7o5k9Z2Y3mNl6ofva6MxsqJk9Zma/ju/rHNUYM3vRzJ40s8fNbE7cNtrMfmdm8+OvTaH72ejMbBMzu9nM5pnZXDPbW+epdpjZjvFnqPv2ppl9Q+coHxSQDdxK4CB3/zDQAhxmZnsBPwCmu/uHgC7gpIB9lMjpwNyC+zpHtelAd28puDz/XOBud98euDu+L2FdBvzW3XcCPkz0udJ5qhHu/pf4M9QC7A68DdyKzlEuKCAbII+siO8Oj28OHATcHLf/DPhUgO5JzMyagSOAq+P7hs5RXhxFdH5A5yk4MxsF7A9cA+Du77n7G+g81aqDgefd/SV0jnJBAdkgxENhjwOLgN8BzwNvuPv78VM6gXGh+icA/Bg4G1gT398UnaNa5MCdZvaImU2L2zZ394Xx968Bm4fpmsS2BRYDP42nAFxtZhui81SrjgV+EX+vc5QDCsgGwd1Xx6nhZmAPYKfAXZICZnYksMjdHwndF+nXfu6+G/AJ4BQz27/wQY8uB9cl4WENA3YD/tPdJwNvUTT0pfNUG+J5sZ8Ebip+TOeodikgq4A4bf97YG9gEzMbFj/UDCwI1jHZF/ikmb0I/JJoqPIydI5qjrsviL8uIprzsgfwNzPbAiD+uihcD4Uom9zp7n+M799MFKDpPNWeTwCPuvvf4vs6RzmggGyAzGysmW0Sfz8S+DjRBNffA8fET5sK/HeYHoq7n+fuze6+DVH6/h53Px6do5piZhua2cbd3wOHAE8BtxGdH9B5Cs7dXwNeMbMd46aDgWfQeapFx7F2uBJ0jnJBhWEHyMwmEU2OHEoU2N7o7heY2XZE2ZjRwGPA5919ZbieCoCZHQB8092P1DmqLfH5uDW+Owz4f+5+kZltCtwIjAdeAj7j7ksDdVMAM2shukBmPeAF4ETi33/oPNWE+J+al4Ht3H1Z3KbPUg4oIBMREREJTEOWIiIiIoEpIBMREREJTAGZiIiISGAKyEREREQCU0AmIiIiEpgCMhFpSGb2KTNzM9MKGyISnAIyEWlUxwF/iL+KiASlgExEGo6ZbQTsB5xEtIoDZjbEzP7DzOaZ2e/M7HYzOyZ+bHczuy9e/PyO7mVoREQqRQGZiDSio4DfuvuzwBIz2x04GtgGmAh8gWhtWsxsOHAFcIy77w7MBC4K0WkRqV/D+n+KiEjdOY5ooXmIltE6juj34U3uvgZ4zcx+Hz++I7AL8Dszg2i5tIXV7a6I1DsFZCLSUMxsNHAQsKuZOVGA5axdT7PXjwBPu/veVeqiiDQgDVmKSKM5Bvi5u2/t7tu4+1bAX4GlQFs8l2xz4ID4+X8BxppZzxCmme0couMiUr8UkIlIozmO3tmwDuDvgE7gGeA64FFgmbu/RxTE/cDMngAeB/apXndFpBGYu4fug4hITTCzjdx9hZltCjwM7Ovur4Xul4jUP80hExFZ69dmtgmwHvCvCsZEpFqUIRMREREJTHPIRERERAJTQCYiIiISmAIyERERkcAUkImIiIgEpoBMREREJDAFZCIiIiKB/X/WQN2GBhjvHQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=data\n",
        "# Creating another figure\n",
        "plt.figure(figsize=(10,6))\n",
        "\n",
        "#plotting the values for people who have heart disease\n",
        "plt.scatter(df.age[df.target==1], \n",
        "            df.chol[df.target==1], \n",
        "            c=\"salmon\") # define it as a scatter figure\n",
        "\n",
        "#plotting the values for people who doesn't have heart disease\n",
        "plt.scatter(df.age[df.target==0], \n",
        "            df.chol[df.target==0], \n",
        "            c=\"lightblue\") # axis always come as (x, y)\n",
        "\n",
        "# Add some helpful info\n",
        "plt.title(\"Heart Disease w.r.t Age and Serum Cholestoral\")\n",
        "plt.xlabel(\"Age\")\n",
        "plt.legend([\"Disease\", \"No Disease\"])\n",
        "plt.ylabel(\"Serum cholestoral\");"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 404
        },
        "id": "c8-tGGSiIQq_",
        "outputId": "63d1f707-8d72-4ce2-81cf-2042594d974e"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x432 with 1 Axes>"
            ],
            "image/png": "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Fz6/hNaZ19A0bXqYQqWw+W8L2PKHm6G1NVqw7p/RdaDvfgdV7HF22203Nm/ezOrVqzss//GPf8zVV1/N4Ycfzvr16xkwYACzZ89m8eLFPPzww7g7H/7wh7nvvvuYPHkyv/jFL9hpp5148803mThxIieffDLLli3jpZde4sknnwRg7dq1AJx55plce+217LHHHjz00EN86UtfYs6cORV7Tj2lQCYiIlJpxWGsu+U1Zsvdf94axtq0trLl7j9XNJB15vDDD+fss8/mlFNO4aSTTmLEiBHMnj2b2bNnc8ABBwCwfv16Fi9ezOTJk7niiiu47bbbAHjxxRdZvHgxe+65J8899xxf+cpX+OAHP8jUqVNZv3498+bN42Mf+1j7Y7311luZP58kFMhERESko3X/TLe8h5577jn69u3LzjvvzNNPP92+/Pzzz+eDH/wgt99+O4cffjh33HEH7s4FF1zAF77whQ7buPfee7nrrrt44IEH2HbbbTnyyCPZuHEjO+64I48//jh33HEH1157LTfddBOXXXYZQ4YMae/HVkvUh0xEREQ6GrxjuuU98Morr/DFL36RL3/5yyXDRCxdupT99tuP8847j4kTJ7Jo0SKOOeYYfvGLX7B+/XoAXnrpJVavXs26devYcccd2XbbbVm0aBEPPvggAC0tLWzZsoWTTz6Ziy++mEcffZQddtiBMWPGcPPNUfOru/P4449X7Dn1hmrIREREKm3M2PLNk2PGVr8sPdDn6OM69iEDaGqiz9HH9Wq7b775JuPHj6e1tZV+/fpx6qmncvbZZ5esd9lll3HPPffQp08f9tlnH4477jj69+/P008/zWGHHQbAdtttx29+8xuOPfZYrr32Wt7znvew5557cuihhwJRYDvjjDPah9X44Q9/CMANN9zA9OnTufjii2ltbeWTn/wk+++/f6+eVyWYu4cuQ49NmDDB58+fH7oYIiIiJUo69o8ZG7RD/9NPP8173vOexOtv/tuCqC/Zun/C4B3pc/RxVek/Vi/K7W8zW+DuZcf2UA2ZiIhIBvJwNmVX+u53kAJYFakPmYiIiEhgCmQiIiIigSmQiYiIiASmQCYiIiISmAKZiIiISGAKZCIiIlIVZsY555zTfv3HP/4x3/ve9xLf/1e/+hXDhg3jgAMOYI899uCYY45h3rx57bd/5zvf4a677qpkkatGgUxERESqon///tx66620tLT0eBuf+MQneOyxx1i8eDHnn38+J510Uvu0SxdddBHvf//7K1XcqlIgExERkRIvrHuDPy9dxa3PvMyfl67ihXVv9Hqb/fr148wzz+TSSy8tuW3ZsmVMmTKFcePGcfTRR/PCCy90u72jjjqKM888kxkzZgBw+umnc8sttwDRfJh7770348aN45vf/CYQTdd08sknM3HiRCZOnMj9998PwMMPP8xhhx3GAQccwKRJk3jmmWcAeOqppzj44IMZP34848aNY/HixQD85je/aV/+hS98gc2bN/d63yiQiYiISAcvrHuDx1at481N0bRDb27awmOr1lUklJ111lnccMMNrFu3rsPyr3zlK5x22mk88cQTnHLKKXz1q19NtL0DDzyQRYsWdVi2Zs0abrvtNp566imeeOIJvv3tbwPwta99jW984xs88sgjzJo1i8997nMA7LXXXvz1r3/lscce46KLLuJb3/oWANdeey1f+9rXWLhwIfPnz2fEiBE8/fTT3Hjjjdx///0sXLiQvn37csMNN/R2t2ikfhEREenoqZbX2Vw0s+Jmj5aPHLxtr7a9ww47MG3aNK644goGDhzYvvyBBx7g1ltvBeDUU0/l3HPPTbS9clNADh48mAEDBvDZz36WE044gRNOOAGAu+66i7///e/t67322musX7+edevWcdppp7F48WLMjNZ4Ds/DDjuM73//+6xYsYKTTjqJPfbYg7vvvpsFCxYwceJEIJqfc+edd+7ZziigQCYiIiIdtNWMJV2e1te//nUOPPBAzjjjjF5v67HHHiuZM7Jfv348/PDD3H333dxyyy1cddVVzJkzhy1btvDggw8yYMCADut/+ctf5qijjuK2225j2bJlHHnkkQB8+tOf5pBDDuFPf/oTxx9/PD/72c9wd0477bT2ycorRU2WIiIi0sHAfuXjQWfL09ppp534+Mc/znXXXde+bNKkSfz2t78F4IYbbuB973tft9uZO3cuM2bM4POf/3yH5W21XscffzyXXnopjz/+OABTp07lyiuvbF9v4cKFAKxbt45dd90ViM7kbPPcc8+x22678dWvfpUTTzyRJ554gqOPPppbbrmF1atXA/Dqq6+yfPnyHuyFjhTIREREpIN9mrenr3Vc1tei5ZVyzjnndDjb8sorr+SXv/wl48aN4/rrr+fyyy8v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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize = (15,15))\n",
        "sns.heatmap(df.corr(), vmin = -1, vmax = +1, annot = True, cmap = 'coolwarm')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 867
        },
        "id": "jnZViXtMIDRC",
        "outputId": "f1c3d35f-67cd-4e7d-c4d6-6bcfe43585da"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1080x1080 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**DATA PRE-PROCESSING**"
      ],
      "metadata": {
        "id": "MlyIhzisDp1Z"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Dataset into dependent and independent features**"
      ],
      "metadata": {
        "id": "9DImCG9p7LYP"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:18.641874Z",
          "iopub.status.busy": "2020-12-11T03:32:18.641084Z",
          "iopub.status.idle": "2020-12-11T03:32:18.644773Z",
          "shell.execute_reply": "2020-12-11T03:32:18.643985Z"
        },
        "papermill": {
          "duration": 0.175986,
          "end_time": "2020-12-11T03:32:18.644942",
          "exception": false,
          "start_time": "2020-12-11T03:32:18.468956",
          "status": "completed"
        },
        "tags": [],
        "id": "iTOVPuarh2hS"
      },
      "outputs": [],
      "source": [
        "y = data[\"target\"]\n",
        "X = data.drop('target',axis=1)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**STANDARDIZATION OF INDEPENDENT VARIABLES**"
      ],
      "metadata": {
        "id": "iBudvXAZ7-_C"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cols=X.columns\n",
        "for col in cols:\n",
        "   X[col]=minmax_scale(X[col])\n",
        "X"
      ],
      "metadata": {
        "id": "vnr2A7Sa7rgs",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "outputId": "d8485834-a7e1-45d9-cc1d-172192525fc3"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           age  sex        cp  trestbps      chol  fbs  restecg   thalach  \\\n",
              "0     0.479167  1.0  0.000000  0.292453  0.196347  0.0      0.5  0.740458   \n",
              "1     0.500000  1.0  0.000000  0.433962  0.175799  1.0      0.0  0.641221   \n",
              "2     0.854167  1.0  0.000000  0.481132  0.109589  0.0      0.5  0.412214   \n",
              "3     0.666667  1.0  0.000000  0.509434  0.175799  0.0      0.5  0.687023   \n",
              "4     0.687500  0.0  0.000000  0.415094  0.383562  1.0      0.5  0.267176   \n",
              "...        ...  ...       ...       ...       ...  ...      ...       ...   \n",
              "1020  0.625000  1.0  0.333333  0.433962  0.216895  0.0      0.5  0.709924   \n",
              "1021  0.645833  1.0  0.000000  0.292453  0.301370  0.0      0.0  0.534351   \n",
              "1022  0.375000  1.0  0.000000  0.150943  0.340183  0.0      0.0  0.358779   \n",
              "1023  0.437500  0.0  0.000000  0.150943  0.292237  0.0      0.0  0.671756   \n",
              "1024  0.520833  1.0  0.000000  0.245283  0.141553  0.0      0.5  0.320611   \n",
              "\n",
              "      exang   oldpeak  slope    ca      thal  \n",
              "0       0.0  0.161290    1.0  0.50  1.000000  \n",
              "1       1.0  0.500000    0.0  0.00  1.000000  \n",
              "2       1.0  0.419355    0.0  0.00  1.000000  \n",
              "3       0.0  0.000000    1.0  0.25  1.000000  \n",
              "4       0.0  0.306452    0.5  0.75  0.666667  \n",
              "...     ...       ...    ...   ...       ...  \n",
              "1020    1.0  0.000000    1.0  0.00  0.666667  \n",
              "1021    1.0  0.451613    0.5  0.25  1.000000  \n",
              "1022    1.0  0.161290    0.5  0.25  0.666667  \n",
              "1023    0.0  0.000000    1.0  0.00  0.666667  \n",
              "1024    0.0  0.225806    0.5  0.25  1.000000  \n",
              "\n",
              "[1025 rows x 13 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ec7ac7fa-d549-4bf1-b97f-a6021cbeb3df\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.479167</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.292453</td>\n",
              "      <td>0.196347</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.740458</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.161290</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.50</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.500000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.433962</td>\n",
              "      <td>0.175799</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.641221</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.854167</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.481132</td>\n",
              "      <td>0.109589</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.412214</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.419355</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.666667</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.509434</td>\n",
              "      <td>0.175799</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.687023</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.687500</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.415094</td>\n",
              "      <td>0.383562</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.267176</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.306452</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1020</th>\n",
              "      <td>0.625000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.333333</td>\n",
              "      <td>0.433962</td>\n",
              "      <td>0.216895</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.709924</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1021</th>\n",
              "      <td>0.645833</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.292453</td>\n",
              "      <td>0.301370</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.534351</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.451613</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1022</th>\n",
              "      <td>0.375000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.150943</td>\n",
              "      <td>0.340183</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.358779</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.161290</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1023</th>\n",
              "      <td>0.437500</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.150943</td>\n",
              "      <td>0.292237</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.671756</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1024</th>\n",
              "      <td>0.520833</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.245283</td>\n",
              "      <td>0.141553</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.320611</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.225806</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1025 rows × 13 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ec7ac7fa-d549-4bf1-b97f-a6021cbeb3df')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ec7ac7fa-d549-4bf1-b97f-a6021cbeb3df button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ec7ac7fa-d549-4bf1-b97f-a6021cbeb3df');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**DIVIDING DATASET INTO TESTING AND TRAINING**\n",
        "\n"
      ],
      "metadata": {
        "id": "Ze--vWyo7bto"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n"
      ],
      "metadata": {
        "id": "KyyEI5HL7gmg"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**AS ALL DATA IS NUMERICAL AND NO CATEGORICAL DATA IS PRESENT WE WONT NEED TO NEED TO ENCODE CATEGORICAL DATA.**"
      ],
      "metadata": {
        "id": "ZXdDZVMNDwTy"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.149344,
          "end_time": "2020-12-11T03:32:18.945832",
          "exception": false,
          "start_time": "2020-12-11T03:32:18.796488",
          "status": "completed"
        },
        "tags": [],
        "id": "7L0WUzVzh2hT"
      },
      "source": [
        "**Before applying algorithm we should check whether the training data is equally splitted or not, because if data is not splitted equally it will cause for data imbalacing problem**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:19.257173Z",
          "iopub.status.busy": "2020-12-11T03:32:19.256029Z",
          "iopub.status.idle": "2020-12-11T03:32:19.261921Z",
          "shell.execute_reply": "2020-12-11T03:32:19.262569Z"
        },
        "papermill": {
          "duration": 0.163698,
          "end_time": "2020-12-11T03:32:19.262751",
          "exception": false,
          "start_time": "2020-12-11T03:32:19.099053",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "osODc58uh2hT",
        "outputId": "bfd21529-ebc0-47b6-d17d-a2b6df845827"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Counter({0: 322, 1: 344})"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ],
      "source": [
        "Counter(y_train)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.15478,
          "end_time": "2020-12-11T03:32:18.319931",
          "exception": false,
          "start_time": "2020-12-11T03:32:18.165151",
          "status": "completed"
        },
        "tags": [],
        "id": "r8pFa6skh2hR"
      },
      "source": [
        "# **MODEL PREPARATION AND EVALUATION**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "papermill": {
          "duration": 0.149107,
          "end_time": "2020-12-11T03:32:19.563256",
          "exception": false,
          "start_time": "2020-12-11T03:32:19.414149",
          "status": "completed"
        },
        "tags": [],
        "id": "_iB5uJJBh2hU"
      },
      "source": [
        " **ML models**\n",
        "\n",
        "Here I take different machine learning algorithm and try to find algorithm which predict accurately.\n",
        "\n",
        "1. Logistic Regression\n",
        "2. Naive Bayes\n",
        "3. Random Forest Classifier\n",
        "4. Extreme Gradient Boost\n",
        "5. K-Nearest Neighbour\n",
        "6. Decision Tree\n",
        "7. Support Vector Machine\n",
        "8. Stacking classifier\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Logistic Regression**"
      ],
      "metadata": {
        "id": "wUHQcOYC63ui"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:19.886758Z",
          "iopub.status.busy": "2020-12-11T03:32:19.884888Z",
          "iopub.status.idle": "2020-12-11T03:32:19.901527Z",
          "shell.execute_reply": "2020-12-11T03:32:19.902246Z"
        },
        "papermill": {
          "duration": 0.188422,
          "end_time": "2020-12-11T03:32:19.902449",
          "exception": false,
          "start_time": "2020-12-11T03:32:19.714027",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qyKQ64oOh2hV",
        "outputId": "40d04cfe-4b31-4cdb-9c20-b9acf3f59a15"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[141  36]\n",
            " [ 17 165]]\n",
            "\n",
            "\n",
            "Accuracy of Logistic Regression: 85.23676880222841 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.89      0.80      0.84       177\n",
            "           1       0.82      0.91      0.86       182\n",
            "\n",
            "    accuracy                           0.85       359\n",
            "   macro avg       0.86      0.85      0.85       359\n",
            "weighted avg       0.86      0.85      0.85       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m1 = 'Logistic Regression'\n",
        "lr = LogisticRegression()\n",
        "model = lr.fit(X_train, y_train)\n",
        "lr_predict = lr.predict(X_test)\n",
        "lr_conf_matrix = confusion_matrix(y_test, lr_predict)\n",
        "lr_acc_score = accuracy_score(y_test, lr_predict)\n",
        "print(\"confussion matrix\")\n",
        "print(lr_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of Logistic Regression:\",lr_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,lr_predict))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Naive Bayes**\n"
      ],
      "metadata": {
        "id": "GAkMv6lh8Yyb"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:20.215287Z",
          "iopub.status.busy": "2020-12-11T03:32:20.214390Z",
          "iopub.status.idle": "2020-12-11T03:32:20.232660Z",
          "shell.execute_reply": "2020-12-11T03:32:20.231564Z"
        },
        "papermill": {
          "duration": 0.178774,
          "end_time": "2020-12-11T03:32:20.232830",
          "exception": false,
          "start_time": "2020-12-11T03:32:20.054056",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vuDd7o6Th2hW",
        "outputId": "a70ae492-def5-4d09-cd36-14d71cc74181"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[139  38]\n",
            " [ 25 157]]\n",
            "\n",
            "\n",
            "Accuracy of Naive Bayes model: 82.45125348189416 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.85      0.79      0.82       177\n",
            "           1       0.81      0.86      0.83       182\n",
            "\n",
            "    accuracy                           0.82       359\n",
            "   macro avg       0.83      0.82      0.82       359\n",
            "weighted avg       0.83      0.82      0.82       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m2 = 'Naive Bayes'\n",
        "nb = GaussianNB()\n",
        "nb.fit(X_train,y_train)\n",
        "nbpred = nb.predict(X_test)\n",
        "nb_conf_matrix = confusion_matrix(y_test, nbpred)\n",
        "nb_acc_score = accuracy_score(y_test, nbpred)\n",
        "print(\"confussion matrix\")\n",
        "print(nb_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of Naive Bayes model:\",nb_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,nbpred))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Random Forest Classifier**"
      ],
      "metadata": {
        "id": "ghP4G2R28dLn"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:20.554045Z",
          "iopub.status.busy": "2020-12-11T03:32:20.543678Z",
          "iopub.status.idle": "2020-12-11T03:32:20.612957Z",
          "shell.execute_reply": "2020-12-11T03:32:20.613663Z"
        },
        "papermill": {
          "duration": 0.229014,
          "end_time": "2020-12-11T03:32:20.613853",
          "exception": false,
          "start_time": "2020-12-11T03:32:20.384839",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nlVjAJwyh2hX",
        "outputId": "37f52556-df7e-4d04-e6f8-983aecf19b5a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[152  25]\n",
            " [ 15 167]]\n",
            "\n",
            "\n",
            "Accuracy of Random Forest: 88.85793871866295 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.91      0.86      0.88       177\n",
            "           1       0.87      0.92      0.89       182\n",
            "\n",
            "    accuracy                           0.89       359\n",
            "   macro avg       0.89      0.89      0.89       359\n",
            "weighted avg       0.89      0.89      0.89       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m3 = 'Random Forest Classfier'\n",
        "rf = RandomForestClassifier(max_depth=5)\n",
        "rf.fit(X_train,y_train)\n",
        "rf_predicted = rf.predict(X_test)\n",
        "rf_conf_matrix = confusion_matrix(y_test, rf_predicted)\n",
        "rf_acc_score = accuracy_score(y_test, rf_predicted)\n",
        "print(\"confussion matrix\")\n",
        "print(rf_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of Random Forest:\",rf_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,rf_predicted))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**XG Boost**"
      ],
      "metadata": {
        "id": "JsraLJjm8lH1"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:20.929923Z",
          "iopub.status.busy": "2020-12-11T03:32:20.928909Z",
          "iopub.status.idle": "2020-12-11T03:32:20.987200Z",
          "shell.execute_reply": "2020-12-11T03:32:20.988106Z"
        },
        "papermill": {
          "duration": 0.222079,
          "end_time": "2020-12-11T03:32:20.988352",
          "exception": false,
          "start_time": "2020-12-11T03:32:20.766273",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZtnmRwPsh2hY",
        "outputId": "a2121cca-dd7a-42d6-a6cb-398f769ec93f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[167  10]\n",
            " [ 15 167]]\n",
            "\n",
            "\n",
            "Accuracy of Extreme Gradient Boost: 93.03621169916435 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.94      0.93       177\n",
            "           1       0.94      0.92      0.93       182\n",
            "\n",
            "    accuracy                           0.93       359\n",
            "   macro avg       0.93      0.93      0.93       359\n",
            "weighted avg       0.93      0.93      0.93       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m4 = 'Extreme Gradient Boost'\n",
        "xgb = XGBClassifier()\n",
        "xgb.fit(X_train, y_train)\n",
        "xgb_predicted = xgb.predict(X_test)\n",
        "xgb_conf_matrix = confusion_matrix(y_test, xgb_predicted)\n",
        "xgb_acc_score = accuracy_score(y_test, xgb_predicted)\n",
        "print(\"confussion matrix\")\n",
        "print(xgb_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of Extreme Gradient Boost:\",xgb_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,xgb_predicted))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**KNN**"
      ],
      "metadata": {
        "id": "qkzybpYF8pPq"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:21.358733Z",
          "iopub.status.busy": "2020-12-11T03:32:21.357902Z",
          "iopub.status.idle": "2020-12-11T03:32:21.376638Z",
          "shell.execute_reply": "2020-12-11T03:32:21.375769Z"
        },
        "papermill": {
          "duration": 0.188796,
          "end_time": "2020-12-11T03:32:21.376787",
          "exception": false,
          "start_time": "2020-12-11T03:32:21.187991",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FQPRUfIVh2hZ",
        "outputId": "18d22824-c02b-466d-b291-bc0880a8b5c6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[158  19]\n",
            " [ 28 154]]\n",
            "\n",
            "\n",
            "Accuracy of K-NeighborsClassifier: 86.90807799442896 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.85      0.89      0.87       177\n",
            "           1       0.89      0.85      0.87       182\n",
            "\n",
            "    accuracy                           0.87       359\n",
            "   macro avg       0.87      0.87      0.87       359\n",
            "weighted avg       0.87      0.87      0.87       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m5 = 'K-NeighborsClassifier'\n",
        "knn = KNeighborsClassifier()\n",
        "knn.fit(X_train, y_train)\n",
        "knn_predicted = knn.predict(X_test)\n",
        "knn_conf_matrix = confusion_matrix(y_test, knn_predicted)\n",
        "knn_acc_score = accuracy_score(y_test, knn_predicted)\n",
        "print(\"confussion matrix\")\n",
        "print(knn_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of K-NeighborsClassifier:\",knn_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,knn_predicted))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Decision Tree**"
      ],
      "metadata": {
        "id": "7DLTjV-Q8sac"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:21.697828Z",
          "iopub.status.busy": "2020-12-11T03:32:21.696975Z",
          "iopub.status.idle": "2020-12-11T03:32:21.714684Z",
          "shell.execute_reply": "2020-12-11T03:32:21.715348Z"
        },
        "papermill": {
          "duration": 0.183294,
          "end_time": "2020-12-11T03:32:21.715510",
          "exception": false,
          "start_time": "2020-12-11T03:32:21.532216",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BhfdAG4Lh2ha",
        "outputId": "e9270bc6-d235-480e-d74d-a3160958946b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[156  21]\n",
            " [ 16 166]]\n",
            "\n",
            "\n",
            "Accuracy of DecisionTreeClassifier: 89.69359331476323 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.91      0.88      0.89       177\n",
            "           1       0.89      0.91      0.90       182\n",
            "\n",
            "    accuracy                           0.90       359\n",
            "   macro avg       0.90      0.90      0.90       359\n",
            "weighted avg       0.90      0.90      0.90       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m6 = 'DecisionTreeClassifier'\n",
        "dt = DecisionTreeClassifier(max_depth=5)\n",
        "dt.fit(X_train, y_train)\n",
        "dt_predicted = dt.predict(X_test)\n",
        "dt_conf_matrix = confusion_matrix(y_test, dt_predicted)\n",
        "dt_acc_score = accuracy_score(y_test, dt_predicted)\n",
        "print(\"confussion matrix\")\n",
        "print(dt_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of DecisionTreeClassifier:\",dt_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,dt_predicted))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Support Vector Classifier**"
      ],
      "metadata": {
        "id": "b55Kajmq8yvF"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:22.042344Z",
          "iopub.status.busy": "2020-12-11T03:32:22.041504Z",
          "iopub.status.idle": "2020-12-11T03:32:22.061353Z",
          "shell.execute_reply": "2020-12-11T03:32:22.060636Z"
        },
        "papermill": {
          "duration": 0.189213,
          "end_time": "2020-12-11T03:32:22.061515",
          "exception": false,
          "start_time": "2020-12-11T03:32:21.872302",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TsfEW5UJh2hb",
        "outputId": "084d6647-219e-4295-de9c-acadf5bb02af"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[154  23]\n",
            " [ 23 159]]\n",
            "\n",
            "\n",
            "Accuracy of Support Vector Classifier: 87.1866295264624 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.87      0.87      0.87       177\n",
            "           1       0.87      0.87      0.87       182\n",
            "\n",
            "    accuracy                           0.87       359\n",
            "   macro avg       0.87      0.87      0.87       359\n",
            "weighted avg       0.87      0.87      0.87       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "m7 = 'Support Vector Classifier'\n",
        "svc =  SVC()\n",
        "svc.fit(X_train, y_train)\n",
        "svc_predicted = svc.predict(X_test)\n",
        "svc_conf_matrix = confusion_matrix(y_test, svc_predicted)\n",
        "svc_acc_score = accuracy_score(y_test, svc_predicted)\n",
        "print(\"confussion matrix\")\n",
        "print(svc_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of Support Vector Classifier:\",svc_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,svc_predicted))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Stacking classifier**"
      ],
      "metadata": {
        "id": "wjU3QtdW86xZ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:25.370393Z",
          "iopub.status.busy": "2020-12-11T03:32:25.369420Z",
          "iopub.status.idle": "2020-12-11T03:32:25.467809Z",
          "shell.execute_reply": "2020-12-11T03:32:25.468803Z"
        },
        "papermill": {
          "duration": 0.268105,
          "end_time": "2020-12-11T03:32:25.469004",
          "exception": false,
          "start_time": "2020-12-11T03:32:25.200899",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LDcI7kObh2hf",
        "outputId": "c5173365-7ba4-42a0-88cc-1d090a01c225"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "confussion matrix\n",
            "[[156  21]\n",
            " [ 15 167]]\n",
            "\n",
            "\n",
            "Accuracy of StackingClassifier: 89.97214484679665 \n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.91      0.88      0.90       177\n",
            "           1       0.89      0.92      0.90       182\n",
            "\n",
            "    accuracy                           0.90       359\n",
            "   macro avg       0.90      0.90      0.90       359\n",
            "weighted avg       0.90      0.90      0.90       359\n",
            "\n"
          ]
        }
      ],
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "estimators = [('rf', RandomForestClassifier(max_depth=5)),('svr' ,LinearSVC())]\n",
        "scv = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())\n",
        "scv.fit(X_train,y_train)\n",
        "scv_predicted = scv.predict(X_test)\n",
        "scv_conf_matrix = confusion_matrix(y_test, scv_predicted)\n",
        "scv_acc_score = accuracy_score(y_test, scv_predicted)\n",
        "print(\"confussion matrix\")\n",
        "print(scv_conf_matrix)\n",
        "print(\"\\n\")\n",
        "print(\"Accuracy of StackingClassifier:\",scv_acc_score*100,'\\n')\n",
        "print(classification_report(y_test,scv_predicted))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:23.114510Z",
          "iopub.status.busy": "2020-12-11T03:32:23.111204Z",
          "iopub.status.idle": "2020-12-11T03:32:23.509234Z",
          "shell.execute_reply": "2020-12-11T03:32:23.508593Z"
        },
        "papermill": {
          "duration": 0.581622,
          "end_time": "2020-12-11T03:32:23.509357",
          "exception": false,
          "start_time": "2020-12-11T03:32:22.927735",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        },
        "id": "HWzP4_xdh2hc",
        "outputId": "f776002e-4a50-4a79-bc82-3ef8e49a23b9"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmEAAAFNCAYAAABIc7ibAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOydeXxcZdmwr7PNnDOTyZ4m3WiBQikUaKEUaCmVIiplFUEWxQXBhU1xecX3dRdR+fyqoqDwVeF9RcFXQBRwwSIUkR0rFWgphaZtkiZtmm2WM3O25/vjTCaTZJK2tMkEeK4f85vlnMy5z5xJc3E/93M/ihBCIJFIJBKJRCIZV9RyByCRSCQSiUTydkRKmEQikUgkEkkZkBImkUgkEolEUgakhEkkEolEIpGUASlhEolEIpFIJGVASphEIpFIJBJJGZASJpFMMJ577jne/e53lzuMCcVpp53G008/XZZjz549m82bN5fl2OXkq1/9KjfddFO5w5BI3tIosk+YRPLGWbZsGZ2dnWiaRiwWY8mSJXzlK18hHo+XO7TdZuPGjXz/+9/n2WefJQgC5s6dyzXXXMNRRx1VlniuvfZaGhsbueaaa8bleNu3b+eHP/whjz32GOl0msbGRpYvX86ll15KLBZj9uzZPPTQQ8yYMWNc4hmJZcuWcd1117Fo0aJ9/t733nsvv/3tb7nzzjv3yfvdf//93HbbbWzatIl4PM4hhxzCJz/5SRYsWLBP3l8ieasgM2ESyV7ys5/9jDVr1nDffffx8ssvc+utt5Y7pJJ4njfstS1btnDhhRcye/ZsHn74Yf7+979zyimn8LGPfYw1a9aMSwzlpKenhwsuuIBcLsddd93FmjVruO222+jr62PLli379FjlPHchBEEQjMuxbrvtNq6//no++clP8o9//INHHnmEiy66iIcffniP32uifV8kkn2OkEgkb5iTTjpJ/OMf/yg8/973vicuu+yywvM1a9aI888/Xxx99NHijDPOEE899VRhW3d3t7j22mvF4sWLxYIFC8SnPvUpIYQQTz31lFiyZIkQQohbbrlFXHXVVYOO+a1vfUt861vfEkII0dfXJ770pS+JxYsXixNOOEGsWLFCeJ4nhBDinnvuEeeff7749re/LRYuXChWrFgxLP7Pf/7z4tJLLx32+le/+lVx0UUXCSGE2Lp1qzj44IPFXXfdJRYvXiwWL14sVq5cWdjX931xyy23iJNPPlksXLhQXH311aK7u3vQz/7v//6vWLp0aeE9r7rqKrFo0SJx1FFHiYsuukhs2LBBCCHEXXfdJQ499FBx2GGHiXnz5olPfOITwz7nG2+8UVx99dXiC1/4gpg3b55Yvny5WLt2bSGeF198UZx11lli3rx54qqrrhKf/vSnS567EEKsWLFCnH766cL3/ZLbhRDi4IMPFr/+9a/FKaecIo4++mjx9a9/XQRBIIQQYvPmzeLiiy8WCxcuFAsXLhSf/exnRW9vb+FnTzrpJHHLLbeI008/XRx22GHCdd3CZzVv3jxx6qmnioceemjQ8X7zm9+I97znPYXtL774ovj85z8vZs+eLQ4//HAxb948ceuttwohRv9+ffCDHxQrVqwQ559/vjj88MNFc3OzuOeee8SyZcvEvHnzxEknnSR+//vfi40bN4q5c+eKQw45RMybN08cffTRQgghvvjFLw763P7617+KM888U8yfP1+cfPLJYvXq1cM+q76+PjFv3jzxxz/+ccTPc+j7Fn/fS31me/M7IJFMdKSESSR7QbEcbNu2TZx++umFPw7t7e1i4cKF4tFHHxW+74vHH39cLFy4UOzcuVMIIcRll10mPv3pT4uenh7hOI54+umnhRCD/yi1tLSII444QiSTSSGEEJ7nicWLF4s1a9YIIYS4/PLLxVe+8hWRTqdFZ2eneN/73ifuvPNOIUQoYXPmzBH/8z//I1zXFbZtD4t/0aJF4u677x72+pNPPikOOeQQYdt2QaSuueYakU6nxfr168Wxxx5bOO/bb79dnHfeeWLbtm0il8uJr3zlK+Kaa64RQgxI2Be+8AWRTqcLMfz2t78VyWRS5HI5cd1114kzzzyzcOyhf6SHfs433nijmDt3rnj00UeF53ni+9//vjjvvPOEEELkcjnxjne8Q9x+++3CcRzxl7/8RRx22GEjSth5550nfvSjH410eYUQoYR9/OMfF729vaK1tVUce+yxBQFpbm4Wjz/+uMjlcmLnzp3ioosuEtddd92guM8880zR1tZWOPc//vGPor29Xfi+Lx588EFx5JFHio6OjsK2E044QbzwwgsiCALR3NwsWlpahn0GQuz6+/XBD35QLF26VGzYsEG4riv6+vrE/PnzxWuvvSaEEKKjo6Mgv/fcc4+44IILBp138XV44YUXxFFHHSUef/xx4fu+aG9vFxs3bhz2Wa1evVrMmTNHuK474ue5OxJW/Jntze+ARDLRkcOREslecsUVVzB//nyWLl1KbW0tV199NQC///3vOfHEE1m6dCmqqrJ48WLmzp3L6tWr2b59O4899hjf+MY3qKqqwjAMFi5cOOy9p06dyqGHHsqqVasAeOqppzBNk3nz5tHZ2cnq1av5z//8T2KxGHV1dXzkIx/hwQcfLPz8pEmTuPjii9F1HdM0h71/d3c3DQ0Nw15vaGggCAJ6e3sHnWd/jdQ555zDAw88AMBdd93FNddcQ1NTE5FIhCuvvJK//OUvg4aSrrrqKmKxWCGGc889l4qKCiKRCFdddRXr168nmUzu9md+9NFHs3TpUjRN46yzzmL9+vUAvPDCC3iex4c+9CEMw+Bd73oXhx9++Ijv09PTU/L8h3LZZZdRWVnJlClTOPbYYwvHmzFjBosXLyYSiVBbW8tHP/pRnn322UE/e/HFFzN58uTCuZ966qk0NjaiqirLly9nxowZrF27FoC7776bSy+9lCOOOAJFUZgxYwZTp04tGdNo369+3vve93LQQQeh6zqapqGqKq+++irZbJZJkyZx0EEH7fLc++N63/vex+LFi1FVlcbGRg488MCSn2dNTQ26ru/W+45E8We2t78DEslEZu9+UyQSCTfddBOLFi3imWee4XOf+xzd3d1UVlbS1tbGn//8Zx555JHCvp7nceyxx9Le3k5VVRVVVVW7fP/TTz+dBx54gLPPPpsHHniA008/HYC2tjY8z+OEE04o7BsEAZMnTy48b2pqGvW9a2pq2LFjx7DXd+zYgaqqVFZWsnPnToBB7zt16lQ2bNhQiOOKK65AVQf+n05V1cLPDY3D931+8IMf8Oc//5murq7Cz3V3d5NIJHb5eQDU19cXHpumSS6Xw/M8tm/fTmNjI4qiFLYXxz2U6urqkuc/lGJRsyyLdDoNQGdnJ9/+9rd57rnnSKfTCCGorKwc9LNDj3/fffdx22230draCkAmk6G7uxuAbdu2sd9+++0yHmDU71epY8diMX7wgx/wi1/8gv/6r//iqKOO4otf/GJJmRrKtm3bWLp06S73q66upru7G8/z9krEhn5me/M7IJFMZKSESST7iIULF3LOOefwve99j5tvvpnJkydz1llncd111w3bd/v27fT29tLX1zfsj/ZQTj31VL73ve/R3t7OX//6V37zm98AFDJPTz311Ih/8IplpBTHH388f/7zn3nf+9436PU//elPzJs3D8uyCq9t27at8Ae7ra2NSZMmFeK4/vrrOfroo4e9f0tLy7A47r//fh5++GFuu+02pk2bRjKZ5JhjjkHkJ2rvKubRaGhooKOjAyFE4X22bdvG9OnTS+5//PHH89e//pUrr7xykETuLitWrEBRFO6//36qq6tZtWoV3/zmNwftU3w+ra2tfPnLX+b2229n/vz5hUxeP5MnT97tCQGjfb9KHRtgyZIlLFmyhGw2yw9/+EO+8pWv8Otf/3qXn/nuxjV//nwikQirVq3iPe95T8l9LMsim80Wnnd2du4y7r35HZBIJjJyOFIi2Yd8+MMf5oknnmD9+vWceeaZPPLII/z973/H931yuRxPP/007e3tTJo0iRNPPJFvfOMb9Pb24rrusGGsfmpra1m4cCFf+tKXmDZtWkGEJk2axOLFi/nud79LKpUiCAK2bNnCM888s9vxXnnllaxZs4Yf/OAH9PT0kEql+OUvf8nvf/97Pv/5zw/a9+abb8a2bV599VXuvfdeli9fDsCFF17ID3/4w0Jmp6urqzB0VIp0Ok0kEqGmpgbbtlmxYsWg7XV1dQV521PmzZuHpmnccccdeJ7HqlWr+Pe//z3i/h/96EdJp9N88YtfLMTf0dHBd77zncKQ42ik02lisRiJRIKOjg5Wrlw56v62baMoCrW1tQDcc889vPrqq4Xt5557Lr/4xS948cUXEUKwefPmQlz19fVs3bq1sO9o369SdHZ2smrVKjKZDJFIhFgsVhDPuro6Ojo6cByn5M+ee+653HvvvTz55JMEQUBHRwevvfbasP0SiQRXX3013/zmN1m1ahW2beO6LqtXr+aGG24AYM6cOaxevZqenh527NjBf//3f4/6mcHY/g5IJOVESphEsg+pra3lrLPO4qabbmLy5MncfPPN3HLLLRx//PEsXbqUn//854VWATfccAO6rnPqqaeyaNGiUf8YnX766TzxxBOFYZh+brjhBlzXZfny5RxzzDFcffXVuzW81s/MmTP59a9/zfr161m2bBlLlizhoYceYuXKlcMyWwsXLuSUU07hIx/5CJdccklhCOhDH/oQy5Yt45JLLmH+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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "lr_false_positive_rate,lr_true_positive_rate,lr_threshold = roc_curve(y_test,lr_predict)\n",
        "nb_false_positive_rate,nb_true_positive_rate,nb_threshold = roc_curve(y_test,nbpred)\n",
        "rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(y_test,rf_predicted)                                                             \n",
        "xgb_false_positive_rate,xgb_true_positive_rate,xgb_threshold = roc_curve(y_test,xgb_predicted)\n",
        "knn_false_positive_rate,knn_true_positive_rate,knn_threshold = roc_curve(y_test,knn_predicted)\n",
        "dt_false_positive_rate,dt_true_positive_rate,dt_threshold = roc_curve(y_test,dt_predicted)\n",
        "svc_false_positive_rate,svc_true_positive_rate,svc_threshold = roc_curve(y_test,svc_predicted)\n",
        "scv_false_positive_rate,scv_true_positive_rate,scv_threshold = roc_curve(y_test,scv_predicted)\n",
        "\n",
        "\n",
        "sns.set_style('whitegrid')\n",
        "plt.figure(figsize=(10,5))\n",
        "plt.title('Reciver Operating Characterstic Curve')\n",
        "plt.plot(lr_false_positive_rate,lr_true_positive_rate,label='Logistic Regression')\n",
        "plt.plot(nb_false_positive_rate,nb_true_positive_rate,label='Naive Bayes')\n",
        "plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Random Forest')\n",
        "plt.plot(xgb_false_positive_rate,xgb_true_positive_rate,label='Extreme Gradient Boost')\n",
        "plt.plot(knn_false_positive_rate,knn_true_positive_rate,label='K-Nearest Neighbor')\n",
        "plt.plot(dt_false_positive_rate,dt_true_positive_rate,label='Desion Tree')\n",
        "plt.plot(svc_false_positive_rate,svc_true_positive_rate,label='Support Vector Classifier')\n",
        "plt.plot(scv_false_positive_rate,scv_true_positive_rate,label='StackingClassifier')\n",
        "plt.plot([0,1],ls='--')\n",
        "plt.plot([0,0],[1,0],c='.5')\n",
        "plt.plot([1,1],c='.5')\n",
        "plt.ylabel('True positive rate')\n",
        "plt.xlabel('False positive rate')\n",
        "plt.legend()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:24.165913Z",
          "iopub.status.busy": "2020-12-11T03:32:24.164684Z",
          "iopub.status.idle": "2020-12-11T03:32:24.168576Z",
          "shell.execute_reply": "2020-12-11T03:32:24.169191Z"
        },
        "papermill": {
          "duration": 0.18048,
          "end_time": "2020-12-11T03:32:24.169348",
          "exception": false,
          "start_time": "2020-12-11T03:32:23.988868",
          "status": "completed"
        },
        "tags": [],
        "id": "rU7vCIADh2hd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "outputId": "086bb1b4-189c-4b39-a8ae-a8406c97394e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    Model   Accuracy\n",
              "1             Naive Bayes  82.451253\n",
              "0     Logistic Regression  85.236769\n",
              "4     K-Nearest Neighbour  86.908078\n",
              "6  Support Vector Machine  87.186630\n",
              "2           Random Forest  88.857939\n",
              "5           Decision Tree  89.693593\n",
              "7      StackingClassifier  89.972145\n",
              "3  Extreme Gradient Boost  93.036212"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c33d8137-67f7-4f05-85ca-0e412d6cf7f3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Model</th>\n",
              "      <th>Accuracy</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Naive Bayes</td>\n",
              "      <td>82.451253</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Logistic Regression</td>\n",
              "      <td>85.236769</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>K-Nearest Neighbour</td>\n",
              "      <td>86.908078</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Support Vector Machine</td>\n",
              "      <td>87.186630</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Random Forest</td>\n",
              "      <td>88.857939</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Decision Tree</td>\n",
              "      <td>89.693593</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>StackingClassifier</td>\n",
              "      <td>89.972145</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Extreme Gradient Boost</td>\n",
              "      <td>93.036212</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c33d8137-67f7-4f05-85ca-0e412d6cf7f3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c33d8137-67f7-4f05-85ca-0e412d6cf7f3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c33d8137-67f7-4f05-85ca-0e412d6cf7f3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ],
      "source": [
        "model_ev = pd.DataFrame({'Model': ['Logistic Regression','Naive Bayes','Random Forest','Extreme Gradient Boost',\n",
        "                    'K-Nearest Neighbour','Decision Tree','Support Vector Machine','StackingClassifier'], 'Accuracy': [lr_acc_score*100,\n",
        "                    nb_acc_score*100,rf_acc_score*100,xgb_acc_score*100,knn_acc_score*100,dt_acc_score*100,svc_acc_score*100,scv_acc_score*100]})\n",
        "model_ev.sort_values(\"Accuracy\", axis = 0, ascending = True,\n",
        "                 inplace = True, na_position ='last')\n",
        "\n",
        "model_ev"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "execution": {
          "iopub.execute_input": "2020-12-11T03:32:24.504377Z",
          "iopub.status.busy": "2020-12-11T03:32:24.503555Z",
          "iopub.status.idle": "2020-12-11T03:32:24.713542Z",
          "shell.execute_reply": "2020-12-11T03:32:24.712783Z"
        },
        "papermill": {
          "duration": 0.381694,
          "end_time": "2020-12-11T03:32:24.713704",
          "exception": false,
          "start_time": "2020-12-11T03:32:24.332010",
          "status": "completed"
        },
        "tags": [],
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "83sf4Up0h2he",
        "outputId": "16d2e459-15d2-4692-8a4c-1516a0671fb2"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1440x720 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABIwAAAJcCAYAAACbuD+6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdebTd873/8ddJTnKCCKKJhOKWVu8pq3qIHDGFiMScGILWGO41VGrWUherlF6uWVmpUkNva0qJeUxNrVKtqb2iRY1JJCTGSE6m7++P/Jzrc5vkhNrnpDwea1kre/y+996fvcjT9/vddVVVVQEAAACA/69TRw8AAAAAwJJFMAIAAACgIBgBAAAAUBCMAAAAACgIRgAAAAAUBCMAAAAACoIRACzEoEGD8vDDD7fLtl577bV89atfzZw5c9ple3x+3HPPPRk4cGCampryzDPPtHn/vffeO9dff32S5Oabb87+++/fetsf//jHDBkyJE1NTbn33nvz5ptvZs8990xTU1P+8z//s2avYUl04YUX5phjjlms+370PQWAfxb1HT0AAPDxXHjhhXn55Zdz1llnLfQ+gwYNyptvvpnOnTtn6aWXzqabbpoTTzwxyyyzTDtOWjvHHXdcVlpppRx55JGLvF9VVRk8eHAaGhpy++23t9N0S5YzzjgjJ554YgYPHvyxH7vjjjtmxx13bL18wQUXZM8998y+++6bJLnooouywgor5PHHH09dXd2nNvPiuOGGG3L99dfn6quvbtftAsDnhT2MAKDGqqrKvHnz2n27o0ePzhNPPJGxY8fmmWeeySWXXPKpb2NJ3yPqsccey7Rp0/Lqq6/m6aefbtdtLynvzcSJE/OVr3ylJs81ceLErLnmmp8oFi0p7w8AsGCCEQAswp/+9Kdsu+222WCDDXL88cenpaUlSfLOO+/koIMOyoYbbpgNNtggBx10UF5//fXWx+29994599xzs8cee2TdddfNq6++mr333jtnn312dt1116y33no55JBD8vbbby9wu5MnT87BBx+c/v37Z6uttsp1112XJHnwwQfzk5/8JHfccUeampqKvT8WplevXtlkk00yfvz41uuefPLJ7LHHHunXr1923HHHPProo8XsC5vzw0Pnrr/++my++eate5qMGTMm22yzTTbYYIMccMABmTBhQpL5sez000/PgAEDst5662WHHXbIX//61yTJrFmzcsYZZ2TzzTfPRhttlJNOOikzZ85Mkjz66KPZbLPN8rOf/SwDBgzIJptskl/96ldJkmuvvTa33HJLLrvssjQ1NeXggw9e6Gu/8cYbM2jQoAwcODBjx44tbnvuuecycuTI9O/fPxtttFFGjx6dJJk7d25Gjx6dwYMHp6mpKTvvvHMmTZq0wMMGP3qo0Q033JA99tgjp59+epqbm3PhhRfmlVdeyT777JPm5uY0Nzfn6KOPzrvvvtv6+EmTJmXUqFHZcMMN09zcnFNOOSWzZs1K//7985e//KX1flOnTs26666badOm/d1rnDdvXi6++OJsscUWGTBgQL773e/mvffey6xZs9LU1JS5c+dm2LBhC93D6Le//W223nrrrL/++jnllFNSVVXrbTfccEO++c1vJkkGDx6cV199NQcffHCamppy1FFHZezYsa2fw8MPP5x58+blkksuyeDBg9Pc3JzDDz/8E6+dJPnqV7+aq6++OkOGDEm/fv3ygx/8IFVV5YUXXsjJJ5+cJ598Mk1NTenXr98CX9tHv4cfrpW33norRx99dNZbb73ssssuee2111rv//jjj2eXXXbJ+uuvn1122SWPP/54622vvvpq9tprrzQ1NWXkyJF56623im0t6jv1US+//HL22muvrL/++mlubs4RRxyxwPsBQIerAIAF2mKLLartttuumjhxYvXWW29Vu+++e3XOOedUVVVV06ZNq+68887qgw8+qN57773qO9/5TnXIIYe0PnavvfaqBg4cWP31r3+tZs+eXc2aNavaa6+9qk022aT6y1/+Uk2fPr0aNWpUdfTRR1dVVVWvvvpqtdZaa1WzZ8+uqqqqvvWtb1Unn3xyNXPmzOqZZ56pmpubq4cffriqqqq64IILWh+3qNl/+9vfVlVVVZMmTaq233776tRTT62qqqpef/31qn///tX9999fzZ07t/rNb35T9e/fv5o6dWrr7G3Neeyxx1bTp0+vZsyYUd1zzz3V4MGDq+eff76aPXt2ddFFF1W77757VVVV9eCDD1Y77bRT9c4771Tz5s2rnn/++Wry5MlVVVXVaaedVh100EHVW2+9Vb333nvVQQcdVJ111llVVVXVI488UjU2NlbnnXdeNWvWrOr++++vvv71r1dvv/12VVVV9b3vfa/1s1iYDz74oGpqaqruv//+6s4776z69+9ftbS0VFVVVe+991618cYbV5dddlk1c+bM6r333quefPLJqqqq6qc//Wm1/fbbVy+88EI1b968avz48dW0adP+7jP68L267rrrqqqqql/96ldVY2NjddVVV1WzZ8+uZsyYUb300kvVb37zm6qlpaWaOnVq9a1vfav64Q9/WFVVVc2ZM6faYYcdqtNOO62aPn16NXPmzOqxxx6rqqqqTj755OrMM89s3c4VV1xRHXTQQQt8nddff301ePDg6pVXXqnef//96tBDD62OOeaY1tvXWmut6qWXXlrgY6dOnVp94xvfqO64445q1qxZ1eWXX141NjYWr2mPPfZovf9H19WCPocrrriiGjFiRDVp0qSqpaWlOvHEE6sjjzyyqqqPv3Y+nP3AAw+s3nnnnWrChAlVc3Nz9cADDyxwtgXZa6+9qsGDB1cvv/xy9e6771bbbLNNNWTIkOq3v/1tNXv27OrYY4+tjjvuuKqqquqtt96q+vXrV914443V7Nmzq1tuuaXq169fNW3atKqqqmq33XarTj/99KqlpaX6/e9/X33jG99o/V4sznfqw/f0yCOPrC6++OJq7ty5xWcOAEsaexgBwCLsueee6du3b5Zffvkccsghue2225IkK6ywQoYOHZqllloq3bt3zyGHHJLHHnuseOxOO+2Ur3zlK6mvr0+XLl2SJMOGDctaa62VpZdeOocffnjuvPPOzJ07t3jcpEmT8vjjj+eYY45JQ0NDGhsbM2LEiNx0000fa/ZDDz00TU1NGThwYHr27JnDDjssSXLTTTdls802y8CBA9OpU6dsvPHGWWeddfLAAw+0PratOb/zne9k6aWXTrdu3XLNNdfkwAMPzJprrpn6+vocfPDBGT9+fCZMmJD6+vpMnz49f/vb31JVVdZcc8307t07VVXluuuuy/e///0sv/zy6d69ew466KDW9zdJ6uvrc+ihh6ZLly4ZOHBgll566bz44ouL/frvvvvudO3aNRtvvHE233zzzJkzp/U13n///fnCF76Q/fffPw0NDenevXvWXXfdJMn111+fww8/PGussUbq6uryr//6r1lhhRUWa5u9e/fO3nvvnfr6+nTr1i2rr756Nt5443Tt2jU9e/bMyJEjW9fJ008/nSlTpuS73/1ull566TQ0NLTuKbPTTjvltttua93b56abblro3mS33HJL9ttvv6y66qpZZpllctRRR+X2229frEO+HnzwwXzlK1/J1ltvnS5dumTffffNF77whcV6rQtyzTXX5Mgjj0yfPn3StWvXjBo1KnfddVcxy+KunQ/9+7//e3r06JGVV145zc3NefbZZz/WTDvvvHNWW221LLvsstlss82y6qqrZqONNkp9fX223nrr1hOB33///Vl99dUzfPjw1NfXZ/vtt88aa6yR++67LxMnTsyf/vSnHH744enatWs22GCDDBo0qHUbi/Od+lB9fX0mTpyYKVOmFJ85ACxpnPQaABahb9++rX9eeeWVM2XKlCTJjBkz8qMf/SgPPfRQ3nnnnSTJ9OnTM3fu3HTu3PnvHruw55s9e/bfHdoyZcqULLfccunevXtx3z//+c8fa/aLLrooG220UX7/+9/n6KOPzltvvZUePXpk4sSJufPOO3Pfffe13nfOnDlpbm5e7Dn79OnT+ueJEyfm9NNPzxlnnNF6XVVVmTx5cgYMGJA999wzp5xySiZMmJAhQ4bke9/7XlpaWjJjxozsvPPOxWM+eq6n5ZdfPvX1//ufKksttVQ++OCDxX79Y8eOzTbbbJP6+vrU19dnyJAhufHGG7PVVltl0qRJWW211Rb4uNdff32ht7Xlo+9Lkrz55ps57bTT8oc//CHTp09PVVXp0aNHkvlhcOWVVy5e44fWXXfddOvWLY8++mh69eqVV155JVtuueUCtzllypSsssoqrZdXWWWVzJkzJ1OnTs1KK620yHmnTJlSzFxXV7fAdbu4Jk6cmEMPPTSdOv3v/5Ps1KlTpk6d2np5cdfOh6+pV69erbcttdRSmT59+sea6aMBrKGhobjcrVu31jU1ZcqUrLzyysVjV1555UyePDlTpkxJjx49svTSSxe3TZo0qfV1tPWd+tCxxx6b888/P7vuumuWW265jBw5MrvuuuvHek0A0B4EIwBYhA//QpjM/0th7969kyQ/+9nP8uKLL+a6665Lr169Mn78+AwfPrw4/8uCTgT80eebNGlSunTpkhVWWKG4vnfv3nnnnXfy/vvvt0ajSZMmtf7l/+OeYLh///7Zeeedc8YZZ+Tiiy9O3759M2zYsPzwhz9crNe9oDk/OkPfvn1z8MEHL3QPmH322Sf77LNPpk6dmiOOOCKXXnppDjvssHTr1i233XZbm1FjQdp6D15//fU88sgjefrpp3P33XcnmR/5Zs2alWnTpqVv374L/dW0Pn365JVXXslaa61VXP9hLJg5c2br5/LGG28scq5zzjkndXV1ueWWW7L88svn3nvvzSmnnJJk/vs2adKkzJkzZ4HRaKeddsrNN9+cXr16ZejQoWloaFjgvL179y72yJk4cWLq6+uz4oorLvT9+VCvXr2Kc29VVVV89h9Xnz59cvrpp2f99df/u9s+PFfQx1k7i/Jp/ypb7969M3HixOK6SZMmZdNNN02vXr3y7rvv5oMPPmhdBxMnTmydYXG+Ux/q1atX6/3+8Ic/ZOTIkdlggw2y+uqrf6qvBwD+UQ5JA4BF+OUvf5nXX389b7/9dkaPHp1tt902yfy9iRoaGtKjR4+8/fbb+fGPf7xYz3fzzTfn+eefz4wZM3L++edn6NChrXskfahv375pamrKOeeck5aWljz77LMZM2ZM61+qV1xxxUyYMOFj/fLavvvum4cffjjPPvtsdtxxx9x333156KGHMnfu3LS0tOTRRx8twsHizPmhPfbYI5dcckmee+65JMl7772XO+64I8n8w66eeuqpzJ49O0sttVS6du2aTp06pVOnThkxYkROP/301r1PJk+enIceemixXs+KK65YnKz4/7rpppvyL//yL7nzzjszduzYjB07NnfddVdWWmml3Hbbbdl8883zxhtv5IorrsisWbPy/vvv56mnnkqSjBgxIueff35eeumlVFWVZ599Nm+99VZ69uyZlVZaKTfddFPmzp2bMWPG5NVXX13knNOnT8/SSy+dZZddNpMnT86ll17aetvXv/719OrVK2effXY++OCDtLS05I9//GPr7TvuuGPuvffe3HzzzRk+fPhCt7H99tvnyiuvzKuvvprp06fn3HPPbd2zqi0DBw7Mc889l7vvvjtz5szJVVddlTfffLPNxy3MN7/5zZx33nmtAWvatGm59957F3r/Ra2dtqy44oqZPHlyZs2a9Ynn/aiBAwfmpZdeyi233JI5c+bk9ttvz/PPP5/NN988q6yyStZZZ51ceOGFmTVrVv7whz8UexMtznfqQ3fccUfr9cstt1zq6uqKPbIAYEnh304AsAjbb7999t9//wwePDirrbZaDjnkkCTzA0xLS0s23HDD7L777tl0000X6/mGDRuW4447LhtvvHFmzZqVE044YYH3O+ecczJhwoRsuummGTVqVL7zne9ko402SpJsvfXWSZLm5ubstNNOi7Xdnj17ZtiwYbnooovSt2/fXHzxxfnJT36SAQMGZODAgbnsssuKALW4cybJVlttlX/7t3/LUUcdlfXWWy/bb799HnzwwSTzg8l//Md/pH///tliiy2y/PLL54ADDkgy/9Cc1VdfPbvttlvWW2+97Lfffot9jqJdd901zz//fPr165dvf/vbf3f7jTfemG9961vp1atX8c8ee+yRG2+8Md27d8/Pfvaz3Hfffdl4440zdOjQ1l+1GjlyZLbZZpvsv//+WW+99XLCCSe0/jreqaeemssuuyzNzc15/vnn09TUtMg5R40alWeeeSb9+vXLgQcemCFDhrTe1rlz54wePTovv/xytthii2y22WZFLOnbt2++9rWvpa6ubpHnudlll12y4447Zq+99sqWW26Zrl275sQTT1ys97Fnz545//zzc/bZZ6e5uTkvv/xy1ltvvcV67ILss88+GTRoUPbff/80NTVlt912y9NPP73Q+y9q7bRlww03zJe//OVssskmCzz06+NaYYUVMnr06Fx++eVpbm7OpZdemtGjR6dnz55JkrPPPjtPPfVUmpubc9FFFxURb3G+Ux/605/+lBEjRqSpqSmHHHJITjjhhKy66qr/8PwA8Gmrqz667zwAUDN77713dtxxx4wYMaKjR1mkf5Y5Pw+OP/749O7dO0ceeWRHjwIAfM44hxEAwBLotddeyz333JMbb7yxo0cBAD6HHJIGALCEOe+887LDDjvkgAMOcLgSANAhHJIGAAAAQMEeRgAAAAAU/inOYfTkk0+moaGho8dgAVpaWnw2WAcksQ6YzzogsQ6YzzogsQ6YzzpYcrW0tOQb3/jGAm/7pwhGDQ0NaWxs7OgxWIDx48f7bLAOSGIdMJ91QGIdMJ91QGIdMJ91sOQaP378Qm9zSBoAAAAABcEIAAAAgIJgBAAAAEBBMAIAAACgIBgBAAAAUBCMAAAAACgIRgAAAAAUBCMAAAAACoIRAAAAAAXBCAAAAICCYAQAAABAQTACAAAAoCAYAQAAAFAQjAAAAAAoCEYAAAAAFAQjAAAAAAqCEQAAAAAFwQgAAACAgmAEAAAAQEEwAgAAAKAgGAEAAABQEIwAAAAAKAhGAAAAABQEIwAAAAAK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av2//vUvNG7cGHv27EFwcDBOnz4NAMjMzMTq1avx8ccfY9euXUhOTsY333wDoCSQ061bN3z55Zfo2bOnktbbb78NBwcHREVFYc2aNQCAy5cvY/To0YiOjoajoyP27t2rfL5OnTqIjIyEn58fJk+ejAULFmD37t344osvcP36dXz33Xdo2bIlvvzyS+zevRsDBgy416eLiIiIHnMMGBEREdFjITo6Gnq9HgDg4eFRbpTR8ePH4eHhAQDo2LEjnJycAADJycno3bs3mjZtCjs7OxgMBiQkJAAAbG1t4e7uXq39t27dGp06dQIA/PGPf8SVK1eUda6ursp+O3TogJYtW8Le3h5t2rRBRkYGOnbsiEOHDmHVqlU4duwYHB0d7+JMEBEREVXN7kFngIiIiOheu3HjBo4cOYLz58/DxsYGFosFNjY2GDVq1F2lW7duXdja2lbrs/b29sr/bW1tUVhYWG6dTqdTfU6n08FsNqNt27aIjIxEXFwcPvjgA/Tt2xdBQUF3lXciIiKiynCEERERET3y9u7dC5PJhP/85z/49ttvERcXh9atWyMjI0P5zIsvvoiYmBgAwIULF3D+/HkAQLdu3ZCQkIDs7GxYLBZER0ejV69eVe7Tzs4ORUVFtZL/zMxM1KtXDyaTCRMnTsSZM2dqJV0iIiIiLRxhRERERI+83bt34y9/+YtqmZubm+qXzEaNGoWQkBB4eHjg+eefR/v27eHo6IiWLVti5syZGDduHEQEzs7OGDRoUJX7HDlyJIxGIzp37oy33nrrrvJ//vx5rFy5EjqdDnZ2dli4cOFdpUdERERUFRsRkQedCSIiIqIHzWKxwGw2o27dukhNTUVAQABiY2NVr4gRERERPS44woiIiIgIQEFBAcaOHQuz2QwRQWhoKINFRERE9NjiCCMiIiIiIiIiIlLhpNdERERERERERKTCgBEREREREREREakwYERERERERERERCoMGBERERERERERkQoDRkREREREREREpPJ/uj0p1nkPmuoAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "colors = ['red','green','blue','gold','silver','yellow','orange','purple']\n",
        "plt.figure(figsize=(20,10))\n",
        "plt.title(\"barplot Represent Accuracy of different models\")\n",
        "plt.ylabel(\"Accuracy %\")\n",
        "plt.xlabel(\"Algorithms\")\n",
        "plt.bar(model_ev['Model'],model_ev['Accuracy'],color = colors)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**CONCLUSION:In general ensembling algorithms perform better than the other.**"
      ],
      "metadata": {
        "id": "nKiRHRMrJhc6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##K-CROSS VALIDATION FOR BEST 4 ALGORITHUM"
      ],
      "metadata": {
        "id": "PkFrRtd7ykEC"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Testing best four Algorithum in k fold cross validation for overfitting**"
      ],
      "metadata": {
        "id": "1hsRFTDt-mWs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "TOP4=[]"
      ],
      "metadata": {
        "id": "wz_kzTGWN8f6"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Decision Tree**"
      ],
      "metadata": {
        "id": "nCJj_6-NQQ8h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "acc1=[]\n",
        "\n",
        "\n",
        "kf=KFold(n_splits=3)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  dt.fit(X_train,y_train)\n",
        "  y_pred = dt.predict(X_test)\n",
        "\n",
        "  acc1.append(accuracy_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",sum(acc1)*100/len(acc1))\n",
        "TOP4.append(sum(acc1)*100/len(acc1))    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LaqaeazO-HuF",
        "outputId": "6f6f6388-594f-4a8a-b2d8-cb8ce98aea8c"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.88      0.92      0.90       158\n",
            "           1       0.93      0.90      0.91       184\n",
            "\n",
            "    accuracy                           0.91       342\n",
            "   macro avg       0.91      0.91      0.91       342\n",
            "weighted avg       0.91      0.91      0.91       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.86      0.89       170\n",
            "           1       0.87      0.93      0.90       172\n",
            "\n",
            "    accuracy                           0.90       342\n",
            "   macro avg       0.90      0.90      0.90       342\n",
            "weighted avg       0.90      0.90      0.90       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.80      0.87       171\n",
            "           1       0.83      0.96      0.89       170\n",
            "\n",
            "    accuracy                           0.88       341\n",
            "   macro avg       0.89      0.88      0.88       341\n",
            "weighted avg       0.89      0.88      0.88       341\n",
            "\n",
            "acc: 89.46196543819633\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Random Forest**"
      ],
      "metadata": {
        "id": "7EhnOwElQZOU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "acc2=[]\n",
        "\n",
        "\n",
        "kf=KFold(n_splits=3)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  rf.fit(X_train,y_train)\n",
        "  y_pred = rf.predict(X_test)\n",
        "\n",
        "  acc2.append(accuracy_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",sum(acc2)*100/len(acc2))\n",
        "TOP4.append(sum(acc2)*100/len(acc2))    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vPnMoJ_EA6q4",
        "outputId": "f204a6cd-a068-4a46-bcf3-28f184bd8b75"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.99      0.92      0.95       158\n",
            "           1       0.93      0.99      0.96       184\n",
            "\n",
            "    accuracy                           0.96       342\n",
            "   macro avg       0.96      0.95      0.96       342\n",
            "weighted avg       0.96      0.96      0.96       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.94      0.87      0.91       170\n",
            "           1       0.88      0.95      0.91       172\n",
            "\n",
            "    accuracy                           0.91       342\n",
            "   macro avg       0.91      0.91      0.91       342\n",
            "weighted avg       0.91      0.91      0.91       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.89      0.90       171\n",
            "           1       0.89      0.92      0.90       170\n",
            "\n",
            "    accuracy                           0.90       341\n",
            "   macro avg       0.90      0.90      0.90       341\n",
            "weighted avg       0.90      0.90      0.90       341\n",
            "\n",
            "acc: 92.29076274916683\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Stacking classifier**"
      ],
      "metadata": {
        "id": "jB95WkhdHSHV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "acc=[]\n",
        "\n",
        "\n",
        "kf=KFold(n_splits=3)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  scv.fit(X_train,y_train)\n",
        "  y_pred = scv.predict(X_test)\n",
        "\n",
        "  acc.append(accuracy_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",sum(acc)*100/len(acc))\n",
        "TOP4.append(sum(acc)*100/len(acc))  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P81w982UIEkF",
        "outputId": "06816e16-52f4-4a34-f484-801ae84ca54b"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.99      0.94      0.96       158\n",
            "           1       0.95      0.99      0.97       184\n",
            "\n",
            "    accuracy                           0.97       342\n",
            "   macro avg       0.97      0.97      0.97       342\n",
            "weighted avg       0.97      0.97      0.97       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.88      0.91       170\n",
            "           1       0.89      0.95      0.92       172\n",
            "\n",
            "    accuracy                           0.92       342\n",
            "   macro avg       0.92      0.91      0.92       342\n",
            "weighted avg       0.92      0.92      0.92       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.90      0.88      0.89       171\n",
            "           1       0.88      0.90      0.89       170\n",
            "\n",
            "    accuracy                           0.89       341\n",
            "   macro avg       0.89      0.89      0.89       341\n",
            "weighted avg       0.89      0.89      0.89       341\n",
            "\n",
            "acc: 92.4845512281845\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Xtreme gradient boosting**"
      ],
      "metadata": {
        "id": "T-ce97WQosPr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "acc3=[]\n",
        "\n",
        "\n",
        "kf=KFold(n_splits=3)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  xgb.fit(X_train,y_train)\n",
        "  y_pred = xgb.predict(X_test)\n",
        "\n",
        "  acc3.append(accuracy_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",sum(acc3)*100/len(acc3))\n",
        "TOP4.append(sum(acc3)*100/len(acc3)) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AEQMNsXNnWPY",
        "outputId": "9df02498-fb8f-4062-d168-3229e4c187e0"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.96      0.97      0.96       158\n",
            "           1       0.97      0.96      0.97       184\n",
            "\n",
            "    accuracy                           0.96       342\n",
            "   macro avg       0.96      0.97      0.96       342\n",
            "weighted avg       0.97      0.96      0.96       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.96      0.91      0.93       170\n",
            "           1       0.91      0.96      0.93       172\n",
            "\n",
            "    accuracy                           0.93       342\n",
            "   macro avg       0.93      0.93      0.93       342\n",
            "weighted avg       0.93      0.93      0.93       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.92      0.92       171\n",
            "           1       0.92      0.92      0.92       170\n",
            "\n",
            "    accuracy                           0.92       341\n",
            "   macro avg       0.92      0.92      0.92       341\n",
            "weighted avg       0.92      0.92      0.92       341\n",
            "\n",
            "acc: 94.04714948008666\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_ev = pd.DataFrame({'Model': ['Decision Tree','Random Forest','StackingClassifier','Extreme Gradient Boost'], 'Accuracy': [TOP4[0],TOP4[1],TOP4[2],TOP4[3]]})\n",
        "model_ev.sort_values(\"Accuracy\", axis = 0, ascending = True,\n",
        "                 inplace = True, na_position ='last')\n",
        "model_ev"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "id": "0AsKtr5DHxHn",
        "outputId": "9e890fc3-0d9d-48d1-d5d1-fe0a579cf3c1"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    Model   Accuracy\n",
              "0           Decision Tree  89.461965\n",
              "1           Random Forest  92.290763\n",
              "2      StackingClassifier  92.484551\n",
              "3  Extreme Gradient Boost  94.047149"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4a729677-17cb-47db-9afd-09ccf0e2b5d8\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Model</th>\n",
              "      <th>Accuracy</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Decision Tree</td>\n",
              "      <td>89.461965</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Random Forest</td>\n",
              "      <td>92.290763</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>StackingClassifier</td>\n",
              "      <td>92.484551</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Extreme Gradient Boost</td>\n",
              "      <td>94.047149</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4a729677-17cb-47db-9afd-09ccf0e2b5d8')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-4a729677-17cb-47db-9afd-09ccf0e2b5d8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-4a729677-17cb-47db-9afd-09ccf0e2b5d8');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "colors = ['red','green','blue','yellow']\n",
        "plt.figure(figsize=(10,10))\n",
        "plt.title(\"barplot Represent Accuracy of different models\")\n",
        "plt.ylabel(\"Accuracy %\")\n",
        "plt.xlabel(\"Algorithms\")\n",
        "plt.bar([\"DECISION TREE\",\"RANDOM FOREST\",\"STACKING CLASSIFIER\",\"XTREME GRADIENT BOOSTING\"],TOP4,color = colors)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621
        },
        "id": "AFBEmEa8O-tf",
        "outputId": "19d7a0b5-20fe-45c8-b3d8-54ad0267b4f7"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x720 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAl4AAAJcCAYAAAAo6aqNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeZjNdf/H8deMWWwNxj3WUET3xB0jTGMJY4x9XwvZ+tmzZI0QQomQlERJd2XLkjVR4iayZOk2upFlMGYYOzNnFp/fH645t2E21fmY5n4+rqvr6mzf8/7O+cyZ53zPmcPNGGMEAAAAl3N/2AMAAAD8ryC8AAAALCG8AAAALCG8AAAALCG8AAAALCG8AAAALCG8kCUEBwdrx44dVu7rzJkzevLJJ5WQkGDl/vC/49tvv1XNmjUVEBCgw4cPp3v9Tp06aenSpZKkr7/+Wt26dXNetnfvXoWGhiogIECbNm3SxYsX1aFDBwUEBOjNN9902T5kRrNmzdKQIUMydN27v6aAK3g87AGArGzWrFk6deqUpk6dmup1goODdfHiRWXLlk05c+ZUjRo1NHr0aOXKlcvipK4zYsQIFSxYUIMGDUrzesYYhYSEyNvbW+vWrbM0Xeby1ltvafTo0QoJCXng2zZt2lRNmzZ1nn733XfVoUMHde7cWZI0e/Zs5cuXT/v27ZObm9ufNnNGLF++XEuXLtWXX35p9X6BzIgjXsBdjDG6ffu29fudM2eOfv75Z61cuVKHDx/W3Llz//T7yOxH6Hbv3q1Lly4pPDxcBw8etHrfmeVrc+7cOZUuXdol2zp37pxKlSr1u6Irs3x9gKyA8EKWcejQITVs2FCVK1fWq6++KofDIUm6evWqevbsqWeffVaVK1dWz549df78eeftOnXqpOnTp6t9+/YqX768wsPD1alTJ02bNk2tW7dWxYoV1bt3b125ciXF+42MjFSvXr1UpUoV1a1bV0uWLJEkbd26VR9++KHWr1+vgICAZEcjUuPn56fq1asrLCzMed7+/fvVvn17VapUSU2bNtWuXbuSzZ7anEkviS5dulS1atVyHvlYtmyZGjRooMqVK6t79+46e/aspDvROWnSJAUFBalixYpq0qSJ/vOf/0iS4uLi9NZbb6lWrVqqWrWqxowZo9jYWEnSrl279Nxzz+njjz9WUFCQqlevrq+++kqStHjxYq1evVrz589XQECAevXqleq+r1ixQsHBwapZs6ZWrlyZ7LKjR4+qa9euqlKliqpWrao5c+ZIkhITEzVnzhyFhIQoICBALVu2VERERIovB9/9EtLy5cvVvn17TZo0SYGBgZo1a5ZOnz6tF198UYGBgQoMDNTgwYN17do15+0jIiLUr18/PfvsswoMDNT48eMVFxenKlWq6Ndff3VeLzo6WuXLl9elS5fu28fbt2/r/fffV+3atRUUFKRhw4bp+vXriouLU0BAgBITE9WsWbNUj3ht375d9evX1zPPPKPx48fr7n94ZPny5Xr++eclSSEhIQoPD1evXr0UEBCgV155RStXrnQ+Djt27NDt27c1d+5chYSEKDAwUAMGDPjda0eSnnzySX355ZcKDQ1VpUqVNG7cOBljdPz4cY0dO1b79+9XQECAKlWqlOK+3f19mLRWLl++rMGDB6tixYpq1aqVzpw547z+vn371KpVKz3zzDNq1aqV9u3b57wsPDxcHTt2VEBAgLp27arLly8nu6+0vqfudurUKXXs2FHPPPOMAgMDNXDgwBSvBzwQA2QBtWvXNo0aNTLnzp0zly9fNu3atTPvvPOOMcaYS5cumQ0bNphbt26Z69evm5dfftn07t3beduOHTuamjVrmv/85z8mPj7exMXFmY4dO5rq1aubX3/91dy8edP069fPDB482BhjTHh4uClTpoyJj483xhjzwgsvmLFjx5rY2Fhz+PBhExgYaHbs2GGMMebdd9913i6t2bdv326MMSYiIsI0btzYTJgwwRhjzPnz502VKlXMli1bTGJiovnXv/5lqlSpYqKjo52zpzfn0KFDzc2bN01MTIz59ttvTUhIiDl27JiJj483s2fPNu3atTPGGLN161bTokULc/XqVXP79m1z7NgxExkZaYwxZuLEiaZnz57m8uXL5vr166Znz55m6tSpxhhjdu7cafz9/c2MGTNMXFyc2bJli3n66afNlStXjDHGDB8+3PlYpObWrVsmICDAbNmyxWzYsMFUqVLFOBwOY4wx169fN9WqVTPz5883sbGx5vr162b//v3GGGM++ugj07hxY3P8+HFz+/ZtExYWZi5dunTfY5T0tVqyZIkxxpivvvrK+Pv7m4ULF5r4+HgTExNjTp48af71r38Zh8NhoqOjzQsvvGDe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+fj4qF69eqpdu7YcDoceeeQRW/MBAABkGWm+1Oju7q7x48c7T3t5eRFdAAAAv1O67/EKCgrSN998I2OMjXkAAACyrHTf47Vo0SJ98skn8vDwkJeXl4wxcnNz0759+2zMBwAAkGWkG14///yzjTkAAACyvHTDa/fu3SmeX7ly5T99GAAAgKws3fCaP3++8/8dDocOHjyosmXLauHChS4dDAAAIKtJN7zmzJmT7HRERIQmTZrksoEAAACyqnT/qvFehQoV0vHjx10xCwAAQJaW7hGvCRMmyM3NTdKdD1QNCwvTU0895fLBAAAAspp0w3eeS5IAACAASURBVKtcuXLO/8+WLZsaNWqkZ555xqVDAQAAZEXphle9evXk7e2tbNmySZISExMVExOjHDlyuHw4AACArCTd93h16dJFsbGxztOxsbHq2rWrS4cCAADIitINL4fDoVy5cjlP58qVSzExMS4dCgAAICtKN7xy5Mihf//7387Tv/zyi7Jnz+7SoQAAALKidN/jNXLkSA0YMEAFChSQMUYXL17U9OnTbcwGAACQpaQbXk8//bTWr1+vEydOSJIef/xxeXp6unwwAACArCbdlxo///xzxcTEqEyZMipTpoxu3bqlzz//3MZsAAAAWUq64bVkyRL5+Pg4T+fJk0dLly516VAAAABZUbrhdfv2bRljnKcTExMVHx/v0qEAAACyonTf41W9enUNHDhQ7du3lyQtWrRINWrUcPlgAAAAWU264TV06FAtXrxYX375pSSpatWqatu2rcsHAwAAyGrSfanR3d1dzz//vN599129++67euKJJzRhwgQbswEAAGQp6R7xkqTDhw9rzZo12rBhg4oWLarQ0FBXzwUAAJDlpBpeJ06c0Nq1a7VmzRrly5dPDRs2lDFGn332mc35AAAAsoxUw6tBgwaqVKmSPvzwQ5UoUUKStGDBAltzAQAAZDmpvsfrvffek5+fn1588UW99tpr+vHHH5N9rAQAAAAeTKpHvEJCQhQSEqJbt25p8+bN+vTTT3Xp0iWNHTtWdevWVfXq1W3OCQAA8JeX7l815syZU02aNNGcOXP0ww8/6KmnntJHH31kYzYAAIAsJUN/1ZgkT548ateundq1a+eqeQAAALKsdI94AQAA4M9BeAEAAFhCeAEAAFhCeAEAAFhCeAEAAFhCeAEAAFhCeAEAAFhC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dzpz5owaNmyokiVLyuFwKFeuXHrhhRfUsmVL5+03bdqkmTNnKiEhQR4eHhowYIBCQkKc216/fr22b9+u3LlzS5ImTpyohQsX6scff5Svr2+y+e99DMeOHauKFSumu66mTJmiggULyuFwqH379urSpYskadasWVqyZEmy+/nss8/k6el533qeOnWq+vTpI0m6ePGi3N3dnbdbunSpvLy8/qyH6Q/74IMPtGbNGrm7u8vd3V3jx4/X3LlzU/2+qVixYoqPfXx8vGbOnKmNGzcqV65c8vLyUp8+fVSzZk0FBwdr2bJl8vX11S+//KL+/fvrvffe05EjR/TLL79ozJgxmjVrlubNm6fvvvtO+fPnl6RkzwcXL17U5MmTtX//fuXJk0eenp566aWXVLdu3fv26cSJE5o0aZJOnTqlXLlyqXjx4ho9erSOHz+ujz/+WB9++GGKX4uU9mv//v2aOHGi4uLiFBcXp4YNG+rll1/WxYsXNWrUKEVERCghIUFFixbVRx99pDNnzjif6+59rsyXL58WLFigWbNmKWfOnOrevXuqzylprcW7RUREqEOHDlq+fLny5s2rq1evqkWLFurRo4e+/PJLSdLp06dVoEABZc+eXU8++aRatWrlnMvhcKh27doaPny4JCW73yTTpk1T9uzZVadOHfXq1UuDBg2SJF26dEk1atRQu3btnI9hSt8jdz9vSNLJkyc1efJkHT9+XD4+PsqVK5f69++vypUrp7vfYWFhat68uT766CM999xzzvPT+5mV9Lint3+vvfaaOnXqJEkaP368ypUrp0OHDmnfvn2Kj4/XmTNn9Pjjj0uSevfurfr16zu3c/f+OxwOBQYGauzYsXJ3d1dcXJzefvttbdmyRW5ubipVqpTGjh3r/BzQ8+fPa9y4cTp+/Lhu376tWrVqadiwYfLy8krxZ2Z6zzGBgYH6+eefdebMmVT3K+m595NPPtHixYvl6ekpNzc3BQUFaciQIfL09LxvvaXI4E9RoUIF5/9fvHjRdO7c2cycOdMYY8zOnTtNjx497rvN7du3Tdu2bc0XX3zhPC8sLMzs3r3bhIeHm0aNGhljjJkzZ46ZNGmS8zrHjx83Docj2f3GxMSYOnXqmG3bthljjLl165bp3r27+ec//2mMMearr74yNWvWNAMGDHBup1GjRiY8PDzF/Ulp5o4dO5qDBw8a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tWqSpEOHDilfvnwqUqSIChYsqJEjR+rKlSvKmzev87Y9e/ZUnz59VKtWrTTv40F+G01St25drV27VgcOHND48ePTvG5qj2Fa1q1bp927d+vEiRMaPXq0vL29nZd16dJF3bt3T3b9P3M925YrVy4tX75ce/bs0a5duzRo0CANHjw4xaMPUuqPfUYEBQVp6dKlql69uvO3/pS8+OKLat68eZpHbcaNG6e9e/fK09NTX331VYbuPy1prel+/fqpadOm+te//qU1a9Zo7dq1+uyzz1SjRg1t2rRJ27Zt09atW9WiRQutWbPmvm1n5LkyteeUtNbivbZu3So/Pz8dPXrU+b2alj179qhp06Y6deqUOnfu7DyqJ92JqzFjxqR4uxo1amjmzJnKnz9/siOaSVL6HklL3759derUKT322GN67733JKW+33f/stWwYUOtWrVK9erVy/B9JUlr/4oVK6by5ctr9erVD7xd6b/7Hx8fr/79+2vt2rV/+Lngz3iOych+bdu2TVOnTtX169c1depUVaxYMUPb5oiXi4SHhytbtmzON72mpHTp0vr3v/+doe3lypVLoaGhev3119W0aVP98MMPyS5/4okn7ttWeHi4cubMmey3Bg8PD3Xr1k0fffTRA+zNf02dOlWbN29WixYtNGHChN+1jawqe/bsWrVqlb7//nsZY/T5559LuvPkd+LECQUHB6tu3bq6ceOGNm7cmOy2jz32mPz9/Z0vC6bm8OHDziePUqVK6Zdffkl2+S+//OJ8aSdJw4YNNXPmTFWrVs35xvmMysi6atiwoVavXq0vv/xS06ZNS/elRin99ZyZZcuWTYGBgerfv79Gjx5932N5t9Qe+xIlSigiIuK+o4Z3S/pBN27cuDTn8fHxUePGjfXFF184zytdurQO3/UveY8dO1YLFizQ5cuX77t9So9xetJb08WLF9cLL7ygBQsW6MiRI877zZs3r5o0aaK3335b//jHP7R79+4Hut/0ZHQthoWFaceOHVqyZIkWLFigqKiodLddqVIlff3111qzZo2WLVuW4X+Y3cvLS2XLltUnn3zyu6LniSeeSPZYzp49W5MnT9bVq1ed56W034mJidq4caNmz56t4OBgvfHGG9q2bVuqay4jP7NS07NnT82bN+93/WKYxNPTUzVq1NDu3btVvHjxFL8//v3vf6t06dIprtkb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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Xtreme Gradient Boosting show the best result from the top 4**"
      ],
      "metadata": {
        "id": "gaH5NSA5LxJ8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**FEATURE SELECTION**"
      ],
      "metadata": {
        "id": "-1urSghcsslB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Feature importance-XG Boost**"
      ],
      "metadata": {
        "id": "D2VlOFpO9LLH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "imp_feature = pd.DataFrame({'Feature': ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',\n",
        "       'exang', 'oldpeak', 'slope', 'ca', 'thal'], 'Importance': xgb.feature_importances_})\n",
        "plt.figure(figsize=(10,4))\n",
        "plt.title(\"barplot Represent feature importance \")\n",
        "plt.xlabel(\"importance \")\n",
        "plt.ylabel(\"features\")\n",
        "plt.barh(imp_feature['Feature'],imp_feature['Importance'],color = 'rgbkymc')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "2NNxo6Rj6JiD",
        "outputId": "88093957-703a-4b6e-fb40-c52154e3ebbe"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAnoAAAEWCAYAAADxdDqwAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deVhV9dr/8fdmBtGUHDtpWWpKamI4lFiGOIM4D+VQ2ckh08p8JCunytIsO5mZPpkNx2OZmh7nk6UeyzQz00zKISdQMQWVwb2Bzff3R0/7F8nkAHv6vK6r64I13vfNkm6+e63vshhjDCIiIiLicXycHYCIiIiIlA41eiIiIiIeSo2eiIiIiIdSoyciIiLiodToiYiIiHgoNXoiIiIiHkqNnoiLi46OZuvWrWVyrqSkJG677TZyc3PL5HzeYOfOnbRv356IiAg2bNjg7HAuyzvvvMOzzz7r7DBE5Cqo0RORKzJr1iyefvrpIreJjo6mcePGRERE0KpVKxISEsjMzCyjCEtfQkICM2fOLHKbN998kwceeIBdu3YRExNzVecry6YfYNiwYbz00ktldr6ilOR6E5FLqdET8RLGGPLy8sr8vO+88w67du1i+fLl7Nu3j3nz5l3zc7jyCOSJEyeoW7eus8MAXLtORXHXuEVcgRo9ETfw448/0rlzZ5o1a8YzzzyDzWYD4Pz58wwdOpSWLVvSrFkzhg4dyqlTpxz7DRw4kJkzZ9KvXz/uuOMOjh8/zsCBA3nttdfo1asXTZs2Zfjw4Zw7d67A86akpDBs2DCaN29Ou3btWLx4MQD//e9/mTt3LmvXriUiIoKuXbsWm0OVKlWIiooiMTHRseyHH36gX79+REZG0rVrV7Zv354v9sLi/OMj5k8//ZQ2bdowePBgAJYsWUKnTp1o1qwZQ4YMITk5Gfi9yZ06dSp33XUXTZs2JS4ujv379wOQnZ3NtGnTaNOmDXfffTcTJkzAarUCsH37du655x7ee+897rrrLqKioli6dCkAn3zyCStXrmT+/PlEREQwbNiwS3KOiYnh+PHjDBs2jIiICLKzs0lPT2f8+PFERUXRunVrZs6cid1uB+DYsWMMGjSIFi1a0KJFC8aMGcOFCxcAGDt2LCdOnHAc63//938d8f3Zn0f9Zs2axahRo3j66adp2rQpn332WZHn/6s/j6L9UfOlS5dy77330qxZMxYtWsSePXuIi4sjMjKSKVOmOPZdtmwZ/fr1Y8qUKdx555107NiRb775xrG+sGuroLg//vjjAq+3pUuX0qlTJyIiImjbti0ff/yx4xhF/ewArFYrr7zyCvfddx933nkn/fv3d/zci7ouRdyOERGXdt9995kuXbqYEydOmLS0NNO3b1/z+uuvG2OMSU1NNevWrTNZWVkmPT3dPP7442b48OGOfQcMGGDuvfdes3//fpOTk2Oys7PNgAEDTFRUlPnll19MZmamGTlypBkzZowxxpjjx4+bevXqmZycHGOMMffff7+ZOHGisVqtZt++faZFixZm69atxhhj3nzzTcd+RcX+9ddfG2OMOXnypImNjTUvvPCCMcaYU6dOmebNm5tNmzYZu91uvvrqK9O8eXNz9uxZR+zFxTl27FiTmZlpLl68aD7//HMTExNjDh48aHJycszs2bNN3759jTHG/Pe//zXdu3c358+fN3l5eebgwYMmJSXFGGPMSy+9ZIYOHWrS0tJMenq6GTp0qJkxY4Yxxpht27aZBg0amDfeeMNkZ2ebTZs2mcaNG5tz584ZY4wZN26c42dRkhoYY8yIESPM888/bzIzM82ZM2dMz549zaJFi4wxxhw5csR89dVXxmazmbNnz5r777/fvPjii4Uea9u2baZ169aFnu/NN9804eHh5vPPPzd2u91cvHixyPP/1Z9/xn/U/PnnnzdWq9Vs2bLFNGzY0AwfPtycOXPGnDp1yrRs2dJs377dGGPM0qVLTYMGDcyCBQtMdna2Wb16tWnatKlJS0szxhR/bf017oKut40bN5qjR4+avLw8s337dtO4cWOzd+/eEv3sJk2aZAYMGGBOnTplcnNzzc6dO43NZiv2uhRxNxrRE3EDDzzwADVq1KBixYoMHz6c1atXA1CpUiU6dOhAcHAwoaGhDB8+nB07duTbt3v37tStWxc/Pz/8/f0BiI+Pp169eoSEhDB69GjWrVt3yajOyZMn+f7773n66acJDAykQYMG9O7dmxUrVlxW7I899hgRERHce++9hIWFMWrUKABWrFjBPffcw7333ouPjw+tWrWiYcOGbN682bFvcXE+/vjjhISEEBQUxMcff8yjjz7Krbfeip+fH8OGDSMxMZHk5GT8/PzIzMzk119/xRjDrbfeStWq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luPsEJyusCd41OSJiIi4DzV6IiIiIh5KjV4B/P39nR2C0xU3Z5DVai2jSERERORK6R69Avj6+mKxWJwdhkszRvcwioiIuDqN6ImIiIh4qFJp9C5cuMDChQuvybHeeecdx9dJSUnExsZek+OKiIiIeLpSa/QWLVp0yfLc3NzLPtbcuXOvRUgiIiIiXqdU7tF77bXXOHbsGPHx8fj5+REYGEiFChU4fPgwa9asYcaMGXz77bdkZ2fzwAMP0K9fP06fPs2TTz5JRkYGdrudSZMmsWnTJqxWK/Hx8dSpU4cnn3yS3NxcxowZw759+6hbty7Tpk0jODiY6OhoOnbsyJYtWwgMDOS1117jpptuYu3atcyePRsfHx/Kly9/zUYaRURERFydxZTCXfVJSUkMGzaMVatWsX37doYOHcrKlSupWbMmn3zyCWfPnmXEiBFkZ2fTr18//vGPf/D5559js9kYPnw4drudixcvEhoaSkREhOONF0lJSbRt25Z//etf3HnnnTzzzDPUqVOHIUOGEB0dTe/evRk+fDjLly9n7dq1zJ07l7i4ON59912qVavGhQsXqFChQrHxJyYmFvmKNfn9YYzC5trzBFarlaAg754z0Ntr4O35g2oAqoG35w/uU4PCZssok6duGzVqRM2aNQH4+uuv+eWXX1i/fj0A6enpHD16lEaNGjF+/Hhyc3OJiYkpNOAaNWpw5513AtC1a1c++ugjhgwZAuC4f69Lly68/PLLAERERJCQkECnTp1o165dqebpbYqbgsWdJSYmenR+JeHtNfD2/EE1ANXA2/MH96hBUQMvZdLohYSEOL42xvDcc8/RunXrS7b75z//yebNm0lISOChhx6iW7dul2zz12lPipsGZcqUKezevZtNmzbRs2dPli5dSqVKla4wExERERH3USoPY5QrV47MzMwC10VFRbFo0SJycn5/zdjhw4fJysoiOTmZypUr06dPH3r37s1PP/0EgJ+fn2NbgBMnTjg+yl21apVjdA9g7dq1AKxZs4aIiAgAjh07xh133MHo0aOpVKkSp06duvYJi4iIiLigUhnRq1SpEk2bNiU2NpbAwEAqV67sWNe7d2+Sk5Pp0aMHxhgqVarE22+/zbfffsv8+fPx8/MjJCSEadOmAdCnTx+6du1KeHg4Tz75JLVr12bhwoWMHz+eOnXq0L9/f8exz58/T1xcHAEBAbz++usATJ8+naNHj2KMoWXLltSvX780UhYRERFxOaXyMIYzREdHs2TJEsLCwq76WHoYo3gectkUyh3uySht3l4Db88fVANQDbw9f3CPGhQVo96MISIiIuKhPOZdt19++eU1O5bdbvf4Eaur5S6Pm4uIiHgzjegV4M8Pf3ir4ubIU5MnIiLi+tToiYiIiHgoj3kY41rau3cfDRvqYQwRERG5MlYrlNWHX0U9jOEx9+hdS76+FoqZh1lERESkUK4yjKaPbkVEREQ8lBo9EREREQ+lRk9ERETEQ3ncPXrLly9n/vz5WCwWbrvtNnx9fQkICGDv3r1kZmaSkJDAfffd5+wwRUREREqdRzV6Bw4cYM6cOSxatIiwsDDOnTvHK6+8QnJyMkuWLOHYsWMMGjSIu+++m8DAQGeHKyIiIh6suDlpy4JHNXrbtm2jY8eOjvfdVqxYEYBOnTrh4+PDzTffTM2aNfn1119d/r11IiIi4t7KqtcoqqH0inv0LH+ZK+Wv34uIiIh4Io9q9Fq2bMm6detIS0sD4Ny5cwCsW7eOvLw8jh07xvHjx6ldu7YzwxQREREpEx710W3dunUZNmwYAwcOxMfHh/Dw399uUaNGDXr16kVmZiaTJ0/W/XkiIiLiFTz+FWgJCQm0adOGjh07lnifxMREwsN1D5+IiIhcmbLsrvQKtMtktxuXeXWJiIiIuJ+yfNdtUTzqHr2CvPLKK5c1mgeQk2MrpWjchys8Eu5M3p4/qAbenj+oBqAaeHv+cOU1cIUmD7yg0RMRERHxVmr0CuAf4O/sEJzOm+cZtOZanR2CiIjINaF79Arg6+OLZbLm2vNWZqJu0BQREc+gET0RERERD6VGT0RERMRDqdETERER8VBu2ehlZWXx6KOP0rVrV2JjY1mzZg179+5lwIAB9OjRgyFDhnD69GnS09Pp0KEDv/76KwBPPfUUixcvdnL0IiIiImXDLR/G2LJlC1WrVmXevHkApKen8/e//523336bsLAw1qxZw8yZM3n55ZeZMGECzzzzDIMGDeL8+fP06dPHydGLO7BarV4/f5S318Db8wfVAFQDb88f3L8Gbtno1atXj2nTpvHqq69y3333UaFCBfbv389DDz0EQF5eHlWqVAGgVatWrFu3jilTprBixQpnhi1uJCgoyKunmIGiX6njDbw9f1ANQDXw9vzBPWpQVCPqlo1e7dq1WbZsGZs3b+aNN96gZcuW1K1bl08++eSSbfPy8jh06BBBQUGcP3+e6tWrOyFiERERkbLnlvfopaSkEBwcTHx8PEOGDGH37t2kpqaya9cuAHJycjhw4AAA77//PrfeeiuvvfYazzzzDDk5Oc4MXURERKTMuOWI3v79+5k+fTo+Pj74+fkxadIk/Pz8ePHFF0lPT8dutzN48GB8fX359NNP+fTTTwkNDaVZs2bMmTOHUaNGOTsFERERkVLnlo1e69atad269SXLFy5ceMmytWvXOr5+5plnSjUuEREREVfilo1eabPn2fUaLC+md92KiIincMt79EpbTrbu43PnR8mvVpBfkLNDEBERuSbU6ImIiIh4KDV6IiIiIh5KjV4BAv39nR2C07nk5JBW3TsnIiJyOfQwRgEsvr5gsTg7DPkrowdkRERELodG9EREREQ8lBo9EREREQ+lRk9ERETEQ7nlPXojRozg1KlT2Gw2Bg0aRN++ffn000959913KV++PPXr1ycgIIAJEyaQmprKxIkTOXHiBADjx4/nzjvvdHIGIiIiIqXPYoz73eF+7tw5KlasiNVqpVevXsyfP5/+/fuzbNkyypUrx+DBg6lfvz4TJkxgzJgx9O/fn8jISE6cOMGQIUPyvRatIImJiTQIDy+jbKTEjCmziZytVitBQd49cbK318Db8wfVAFQDb88f3KcGhc2W4ZYjeh999BGff/45ACdPnmTFihU0a9aMihUrAtCxY0eOHDkCwNatWzl48KBj34yMDDIzMylXrlyZxy1Xr6ymfUlMTHTNKWbKkLfXwNvzB9UAVANvzx/cowZFDYK4XaO3fft2tm7dyieffEJwcDADBw7klltu4dChQwVun5eXx+LFiwkMDCzjSEVEREScy+0exkhPT+e6664jODiYQ4cO8cMPP5CVlcWOHTs4f/48ubm5/Oc//3FsHxUVxUcffeT43pvf4SoiIiLexe0avXvuuYfc3Fw6derEa6+9RpMmTahWrRpDhw6ld+/e9O/fn7/97W+UL18egGeffZa9e/cSFxdH586dWbRokZMzEBERESkbbvfRbUBAAO++++4lyxs2bEjfvn3Jzc1l5MiRxMTEABAWFsYbb7xR1mGKiIiIOJ3bNXqFeeutt9i6dSs2m42oqChHo3cljN2u1225IqsV3ODJJxEREVfhMY3euHHjrtmxbDk51+xY7solnzJSkyciInJZ3O4ePREREREpGTV6IiIiIh5KjZ6IiIiIh1KjJyIiIuKh1OiJiIiIeCg1eiIiIiIeSo2eiIiIiIdSoyciIiLioSzG6BUQf/XDDz8QGBjo7DBEREREimWz2WjSpEmB69ToiYiIiHgofXQrIiIi4qHU6ImIiIh4KDV6IiIiIh5KjZ6IiIiIh1KjJyIiIuKh1OiJiIiIeCiPb/T++9//0qFDB9q1a8e8efMuWZ+dnc0TTzxBu3bt6N27N0lJSY51c+fOpV27dnTo0IEtW7aU+Jiu5kpr8PXXX9OjRw/i4uLo0aMH33zzjWOfgQMH0qFDB+Lj44mPj+fs2bNlls+VuNIaJCUl0bhxY0eeEyZMcOyzd+9e4uLiaNeuHS+++CKuPFPRleb/73//25F7fHw89evXJzExEfC8a2DHjh10796d8PBw1q1bl2/dZ599Rvv27Wnfvj2fffaZY7knXQOF5Z+YmEjfvn3p0qULcXFxrFmzxrEuISGB6OhoxzXwx7Xhqq7mGmjQoIEjz2HDhjmWHz9+nN69e9OuXTueeOIJsrOzSz2Pq3GlNdi2bVu+3wWNGjViw4YNgHtdB8Xlv2DBAjp37kxcXByDBw8mOTnZsc5tfw8YD5abm2vatm1rjh07Zmw2m4mLizMHDhzIt80///lP8/zzzxtjjFm1apUZPXq0McaYAwcOmLi4OGOz2cyxY8dM27ZtTW5ubomO6UqupgY//fSTOXXqlDHGmF9++cVERUU59hkwYIDZs2dPGWVxda6mBsePHzddunQp8Lg9e/Y0u3btMnl5eWbIkCFm06ZNpZvIFbqa/P/s559/Nm3btnV872nXwPHjx01iYqIZO3asWbt2rWN5WlqaiY6ONmlpaebcuXMmOjranDt3zhjjWddAYfn/+uuv5vDhw8YYY06dOmVatWplzp8/b4wxZty4cfm2dWVXUwNjjGnSpEmBxx01apRZtWqVMcaY559/3ixcuLB0ErgGrrYGf0hLSzPNmjUzWVlZxhj3uQ5Kkv8333zjyGvhwoWO34Xu/HvAo0f09uzZw0033UTNmjUJCAigS5cufPHFF/m2+fLLL+nevTsAHTp04JtvvsEYwxdffEGXLl0ICAigZs2a3HTTTezZs6dEx3QlV1OD8PBwqlWrBkDdunWx2Wwu/9dqQa6mBoU5ffo0GRkZNGnSBIvFQrdu3Vz2OrhW+a9evZouXbqUWdzXUklqcOONN1K/fn18fPL/Wvzqq69o1aoVFStW5LrrrqNVq1Zs2bLF466BwvKvXbs2N998MwDVqlUjLCyM1NTUsgr9mrmaGhTGGMO2bdvo0KEDAN27d3fZawCuXQ3Wr19P69atCQ4OLu2Qr6mS5N+yZUtHXk2aNOHUqVOAe/8e8OhGLyUlherVqzu+r1atGikpKZdsU6NGDQD8/PwoX748aWlphe5bkmO6kqupwZ+tX7+e8PBwAgICHMvGjx9PfHw8s2fPdr2h6j+52hokJSXRrVs3BgwYwHfffVfgMatXr+6y18G1ugbWrFlzSaPnSdfA5e7raddASezZs4ecnBxq1arlWDZz5kzi4uKYOnWqS/8heLU1sNls9OjRgz59+jg+skxLS6NChQr4+fkBrn0NwLW7DlavXk1sbGy+Ze5wHVxu/kuWLOGee+4pcl93+D3g5+wAxPUdOHCAGTNm8N577zmWzZgxg2rVqpGRkcGoUaNYsWIF3bp1c2KUpaNq1aps3LiRSpUqsXfvXh577DFWr17t7LDK3O7duwkODqZevXqOZd5yDcjvTp8+zdixY5k2bZpjtOepp56iSpUq5OTk8PzzzzNv3jxGjhzp5EhLx8aNG6lWrRrHjx9n8ODB1KtXj9DQUGeHVeZOnz7N/v37iYqKcizzxOtgxYoV7N27l3/+85/ODuWqefSIXrVq1RzDrvB7R/7HR5F/3ubkyZMA5Obmkp6eTqVKlQrdtyTHdCVXUwOAU6dOMXLkSKZNm5bvr/g/jhEaGkpsbCx79uwp7VSu2NXUICAgwFGLhg0bUqtWLQ4fPnzJMU+dOuWy18HVXgNQ8Me2nnYNXO6+nnYNFCUjI4OhQ4fy5JNP5ntxetWqVbFYLAQEBNCjRw9+/PHHaxr3tXS1Nfhj25o1a9K8eXP27dtHpUqVuHDhArm5uYBrXwNw9TUAWLt2Le3atcPf39+xzF2ug5Lmv3XrVt555x3mzJnj+BTLnX8PeHSj16hRI44cOcLx48fJzs5m9erVREdH59smOjra8fTM+vXradmyJRaLhejoaFavXk12djbHjx/nyJEjNG7cuETHdCVXU4MLFy7w6KOPMmbMGO68807H9rm5uY57dHJycti0aRN169Ytu6Qu09XUIDU1FbvdDuC4DmrWrEnVqlUJDQ3lhx9+wBjD8uXLadu2bZnnVhJXkz9AXl4ea9euzdfoeeI1UJioqCi++uorzp8/z/nz5/nqq6+IioryuGugMNnZ2Tz22GPEx8fTsWPHfOtOnz4N/H6v2oYNGzz2Gjh//rzj48jU1FS+//576tSpg8VioUWLFqxfvx74/alMd///QXEK+qPPXa6DkuS/b98+JkyYwJw5c7j++usdy93694BzngEpO5s2bTLt27c3bdu2NW+//bYxxpg33njDbNiwwRhjjNVqNY8//riJiYkxPXv2NMeOHXPs+/bbb5u2bdua9u3b53uKpqBjurIrrcHs2bPNHXfcYbp27er478yZMyYzM9N0797dxMbGms6dO5sXXnjB5ObmOi2/krjSGqxbt8507tzZdO3a1XTr1s188cUXjmPu2bPHdOnSxbRt29ZMnjzZ5OXllX1iJXQ1/w62bdtmevfune94nngN7N6927Ru3drccccdpnnz5qZz586OfT/99FMTExNjYmJizJIlSxzLPekaKCz/5cuXm/Dw8Hy/B/bt22eMMWbgwIEmNjbWdOnSxYwZM8ZkZGQ4J7kSutIa7Ny508TGxpq4uDgTGxtrFi9e7DjmsWPHTM+ePU1MTIx5/PHHjc1mK/vELsPV/Ds4fvy4iYqKMna7Pd8x3ek6KC7/wYMHm7vuustxrQ8dOtSxr7v+HrAY48J3UIuIiIjIFfPoj25FREREvJkaPREREREPpUZPRERExEOp0RMRERHxUGr0RERERDyUGj0R8Ur9+vUr0/MlJSWxcuXKMj2niIgaPRHxSh9//HGZnSs3N5fk5GRWrVpVZucUEQHQPHoi4pUiIiLYtWsX27dvZ9asWZQvX579+/fTqVMn6tWrx4cffojNZmP27NnUqlWLhIQEAgIC2Lt3L5mZmSQkJHDfffdhs9mYNGkSe/fuxdfXl4SEBFq2bMmyZcv4z3/+Q1ZWFnl5eWRnZ3Po0CFuvPFGunfvTkxMDP/zP//DxYsXAXj++edp2rQp27dv56233qJSpUrs37+f22+/nRkzZmCxWNizZw9Tp04lKyuLgIAA3n//fYKDg5kxYwbffvst2dnZPPDAA2U+WikirsvP2QGIiDjbzz//zJo1a6hYsSJt27ald+/eLFmyhA8++ICPPvqIZ599FoDk5GSWLFnCsWPHGDRoEHfffTcLFy4EYOXKlRw6dIghQ4Y4Xom1b98+/v3vf1OxYkW2b9/Oe++9x9y5cwG4ePEiCxYsIDAwkCNHjvDUU0+xbNkyx36rV6+matWq9O/fn507d9K4cWOefPJJZs6cSePGjcnIyCAoKIglS5ZQvnx5li5dSnZ2Nv369aNVq1bUrFnTCZUUEVejRk9EvF6jRo2oWrUqALVq1aJVq1YA1KtXj+3btzu269SpEz4+Ptx8883UrFmTX3/9lZ07dzJgwAAAbr31Vm644QYOHz4MQKtWrahYsWKB58zNzWXKlCn8/PPP+Pj4cOTIEce6xo0bU716dQDq169PcnIy5cuXp0qVKjRu3BiA0NBQAL7++mt++eUXR3OZnp7O0aNH1eiJCKBGT0SEgIAAx9c+Pj6O7318fLDb7Y51Fosl335//f6vgoODC133/vvvU7lyZVasjgeUdQAAAWFJREFUWEFeXp6jgftrPL6+vvli+CtjDM899xytW7cuMhYR8U56GENEpITWrVtHXl4ex44d4/jx49SuXZvIyEjH07SHDx/m5MmT3HLLLZfsW65cOTIzMx3fp6enU6VKFXx8fFixYkWRzRxA7dq1+e2339izZw8AGRkZ5ObmEhUVxaJFi8jJyXHEkJWVda1SFhE3pxE9EZESqlGjBr169SIzM5PJkycTGBjI/fffz6RJk4iLi8PX15eXX34534jcH2677TZ8fHzo2rUrPXr04P777+fxxx9n+fLltG7dmpCQkCLPHRAQwMyZM3nxxRexWq0EBQWxYMECevfuTXJyMj169MAYQ6VKlXj77bdLqwQi4mb01K2ISAkkJCTQpk0bOnbs6OxQRERKTB/dioiIiHgojeiJiIiIeCiN6ImIiIh4KDV6IiIiIh5KjZ6IiIiIh1KjJyIiIuKh1OiJiIiIeKj/B0xTk6DbjJrrAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Conclusion**\n",
        "\n",
        "*  'fbs' has least importance in the boosting\n",
        "*   'cp' and 'thal' have maximum inportance in the boosting \n",
        "\n"
      ],
      "metadata": {
        "id": "9G4YkAQeGdDF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Let's drop the least important feature and see the impact on performance**"
      ],
      "metadata": {
        "id": "Ykf9VqzwGxiL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Default dataset**"
      ],
      "metadata": {
        "id": "EDPXIGB0Ype6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = data[\"target\"]\n",
        "X = data.drop(columns=['target'])\n",
        "cols=X.columns\n",
        "for col in cols:\n",
        "   X[col]=minmax_scale(X[col])\n",
        "X"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "nVRB4Z7OgvAN",
        "outputId": "8add111d-09ce-4d5b-c723-777b85b3e0a0"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           age  sex        cp  trestbps      chol  fbs  restecg   thalach  \\\n",
              "0     0.479167  1.0  0.000000  0.292453  0.196347  0.0      0.5  0.740458   \n",
              "1     0.500000  1.0  0.000000  0.433962  0.175799  1.0      0.0  0.641221   \n",
              "2     0.854167  1.0  0.000000  0.481132  0.109589  0.0      0.5  0.412214   \n",
              "3     0.666667  1.0  0.000000  0.509434  0.175799  0.0      0.5  0.687023   \n",
              "4     0.687500  0.0  0.000000  0.415094  0.383562  1.0      0.5  0.267176   \n",
              "...        ...  ...       ...       ...       ...  ...      ...       ...   \n",
              "1020  0.625000  1.0  0.333333  0.433962  0.216895  0.0      0.5  0.709924   \n",
              "1021  0.645833  1.0  0.000000  0.292453  0.301370  0.0      0.0  0.534351   \n",
              "1022  0.375000  1.0  0.000000  0.150943  0.340183  0.0      0.0  0.358779   \n",
              "1023  0.437500  0.0  0.000000  0.150943  0.292237  0.0      0.0  0.671756   \n",
              "1024  0.520833  1.0  0.000000  0.245283  0.141553  0.0      0.5  0.320611   \n",
              "\n",
              "      exang   oldpeak  slope    ca      thal  \n",
              "0       0.0  0.161290    1.0  0.50  1.000000  \n",
              "1       1.0  0.500000    0.0  0.00  1.000000  \n",
              "2       1.0  0.419355    0.0  0.00  1.000000  \n",
              "3       0.0  0.000000    1.0  0.25  1.000000  \n",
              "4       0.0  0.306452    0.5  0.75  0.666667  \n",
              "...     ...       ...    ...   ...       ...  \n",
              "1020    1.0  0.000000    1.0  0.00  0.666667  \n",
              "1021    1.0  0.451613    0.5  0.25  1.000000  \n",
              "1022    1.0  0.161290    0.5  0.25  0.666667  \n",
              "1023    0.0  0.000000    1.0  0.00  0.666667  \n",
              "1024    0.0  0.225806    0.5  0.25  1.000000  \n",
              "\n",
              "[1025 rows x 13 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-06f9b27c-282b-4eed-af0e-73c1b7fe2dd6\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.479167</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.292453</td>\n",
              "      <td>0.196347</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.740458</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.161290</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.50</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.500000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.433962</td>\n",
              "      <td>0.175799</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.641221</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.854167</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.481132</td>\n",
              "      <td>0.109589</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.412214</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.419355</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.666667</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.509434</td>\n",
              "      <td>0.175799</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.687023</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.687500</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.415094</td>\n",
              "      <td>0.383562</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.267176</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.306452</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1020</th>\n",
              "      <td>0.625000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.333333</td>\n",
              "      <td>0.433962</td>\n",
              "      <td>0.216895</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.709924</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1021</th>\n",
              "      <td>0.645833</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.292453</td>\n",
              "      <td>0.301370</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.534351</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.451613</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1022</th>\n",
              "      <td>0.375000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.150943</td>\n",
              "      <td>0.340183</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.358779</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.161290</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1023</th>\n",
              "      <td>0.437500</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.150943</td>\n",
              "      <td>0.292237</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.671756</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1024</th>\n",
              "      <td>0.520833</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.245283</td>\n",
              "      <td>0.141553</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.320611</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.225806</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1025 rows × 13 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-06f9b27c-282b-4eed-af0e-73c1b7fe2dd6')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-06f9b27c-282b-4eed-af0e-73c1b7fe2dd6 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-06f9b27c-282b-4eed-af0e-73c1b7fe2dd6');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "acc1=[]\n",
        "p1=[]\n",
        "r1=[]\n",
        "f1=[]\n",
        "hmsc=[]\n",
        "model=XGBClassifier()\n",
        "\n",
        "kf=KFold(n_splits=4,shuffle=False)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  model.fit(X_train,y_train)\n",
        "  y_pred = model.predict(X_test)\n",
        "\n",
        "  acc1.append(accuracy_score(y_test,y_pred))\n",
        "  p1.append(precision_score(y_test,y_pred))\n",
        "  r1.append(recall_score(y_test,y_pred))\n",
        "  f1.append(f1_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",(sum(acc1)*100/len(acc1)))\n",
        "hmsc.extend(((sum(acc1)*100/len(acc1)),(sum(p1)*100/len(p1)),(sum(r1)*100/len(r1)),(sum(f1)*100/len(f1))))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bkqLUbHNY1ql",
        "outputId": "5a949a37-7a3a-4abb-edd7-f42068afbfc4"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.96      0.96       126\n",
            "           1       0.96      0.95      0.96       131\n",
            "\n",
            "    accuracy                           0.96       257\n",
            "   macro avg       0.96      0.96      0.96       257\n",
            "weighted avg       0.96      0.96      0.96       257\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.94      0.97      0.96       114\n",
            "           1       0.98      0.95      0.96       142\n",
            "\n",
            "    accuracy                           0.96       256\n",
            "   macro avg       0.96      0.96      0.96       256\n",
            "weighted avg       0.96      0.96      0.96       256\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.98      0.94      0.96       126\n",
            "           1       0.95      0.98      0.96       130\n",
            "\n",
            "    accuracy                           0.96       256\n",
            "   macro avg       0.96      0.96      0.96       256\n",
            "weighted avg       0.96      0.96      0.96       256\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.98      0.96       133\n",
            "           1       0.97      0.94      0.96       123\n",
            "\n",
            "    accuracy                           0.96       256\n",
            "   macro avg       0.96      0.96      0.96       256\n",
            "weighted avg       0.96      0.96      0.96       256\n",
            "\n",
            "acc: 96.00027358949417\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Changed features**"
      ],
      "metadata": {
        "id": "TeMx11Sib2g6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = data[\"target\"]\n",
        "X = data.drop(columns=['target','fbs'])\n",
        "cols=X.columns\n",
        "for col in cols:\n",
        "   X[col]=minmax_scale(X[col])\n",
        "X"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "aGcwFNuBXzdd",
        "outputId": "711f0ed0-b6ae-4b3b-e822-a9c7194deab3"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           age  sex        cp  trestbps      chol  restecg   thalach  exang  \\\n",
              "0     0.479167  1.0  0.000000  0.292453  0.196347      0.5  0.740458    0.0   \n",
              "1     0.500000  1.0  0.000000  0.433962  0.175799      0.0  0.641221    1.0   \n",
              "2     0.854167  1.0  0.000000  0.481132  0.109589      0.5  0.412214    1.0   \n",
              "3     0.666667  1.0  0.000000  0.509434  0.175799      0.5  0.687023    0.0   \n",
              "4     0.687500  0.0  0.000000  0.415094  0.383562      0.5  0.267176    0.0   \n",
              "...        ...  ...       ...       ...       ...      ...       ...    ...   \n",
              "1020  0.625000  1.0  0.333333  0.433962  0.216895      0.5  0.709924    1.0   \n",
              "1021  0.645833  1.0  0.000000  0.292453  0.301370      0.0  0.534351    1.0   \n",
              "1022  0.375000  1.0  0.000000  0.150943  0.340183      0.0  0.358779    1.0   \n",
              "1023  0.437500  0.0  0.000000  0.150943  0.292237      0.0  0.671756    0.0   \n",
              "1024  0.520833  1.0  0.000000  0.245283  0.141553      0.5  0.320611    0.0   \n",
              "\n",
              "       oldpeak  slope    ca      thal  \n",
              "0     0.161290    1.0  0.50  1.000000  \n",
              "1     0.500000    0.0  0.00  1.000000  \n",
              "2     0.419355    0.0  0.00  1.000000  \n",
              "3     0.000000    1.0  0.25  1.000000  \n",
              "4     0.306452    0.5  0.75  0.666667  \n",
              "...        ...    ...   ...       ...  \n",
              "1020  0.000000    1.0  0.00  0.666667  \n",
              "1021  0.451613    0.5  0.25  1.000000  \n",
              "1022  0.161290    0.5  0.25  0.666667  \n",
              "1023  0.000000    1.0  0.00  0.666667  \n",
              "1024  0.225806    0.5  0.25  1.000000  \n",
              "\n",
              "[1025 rows x 12 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e6864cb6-c0c0-4229-95d3-b78d91b0d509\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.479167</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.292453</td>\n",
              "      <td>0.196347</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.740458</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.161290</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.50</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.500000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.433962</td>\n",
              "      <td>0.175799</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.641221</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.854167</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.481132</td>\n",
              "      <td>0.109589</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.412214</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.419355</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.666667</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.509434</td>\n",
              "      <td>0.175799</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.687023</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.687500</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.415094</td>\n",
              "      <td>0.383562</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.267176</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.306452</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1020</th>\n",
              "      <td>0.625000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.333333</td>\n",
              "      <td>0.433962</td>\n",
              "      <td>0.216895</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.709924</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1021</th>\n",
              "      <td>0.645833</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.292453</td>\n",
              "      <td>0.301370</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.534351</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.451613</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1022</th>\n",
              "      <td>0.375000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.150943</td>\n",
              "      <td>0.340183</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.358779</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.161290</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1023</th>\n",
              "      <td>0.437500</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.150943</td>\n",
              "      <td>0.292237</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.671756</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.666667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1024</th>\n",
              "      <td>0.520833</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.245283</td>\n",
              "      <td>0.141553</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.320611</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.225806</td>\n",
              "      <td>0.5</td>\n",
              "      <td>0.25</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1025 rows × 12 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e6864cb6-c0c0-4229-95d3-b78d91b0d509')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e6864cb6-c0c0-4229-95d3-b78d91b0d509 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e6864cb6-c0c0-4229-95d3-b78d91b0d509');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "acc1=[]\n",
        "p1=[]\n",
        "r1=[]\n",
        "f1=[]\n",
        "msc=[]\n",
        "model=XGBClassifier()\n",
        "\n",
        "kf=KFold(n_splits=4,shuffle=False)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  model.fit(X_train,y_train)\n",
        "  y_pred = model.predict(X_test)\n",
        "\n",
        "  acc1.append(accuracy_score(y_test,y_pred))\n",
        "  p1.append(precision_score(y_test,y_pred))\n",
        "  r1.append(recall_score(y_test,y_pred))\n",
        "  f1.append(f1_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",(sum(acc1)*100/len(acc1)))\n",
        "msc.extend(((sum(acc1)*100/len(acc1)),(sum(p1)*100/len(p1)),(sum(r1)*100/len(r1)),(sum(f1)*100/len(f1))))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D-61cWfvZJG8",
        "outputId": "f38ad79f-895c-4d03-e387-1adf537b30cd"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.97      0.96       126\n",
            "           1       0.97      0.95      0.96       131\n",
            "\n",
            "    accuracy                           0.96       257\n",
            "   macro avg       0.96      0.96      0.96       257\n",
            "weighted avg       0.96      0.96      0.96       257\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.93      0.97      0.95       114\n",
            "           1       0.98      0.94      0.96       142\n",
            "\n",
            "    accuracy                           0.96       256\n",
            "   macro avg       0.96      0.96      0.96       256\n",
            "weighted avg       0.96      0.96      0.96       256\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.98      0.94      0.96       126\n",
            "           1       0.95      0.98      0.96       130\n",
            "\n",
            "    accuracy                           0.96       256\n",
            "   macro avg       0.96      0.96      0.96       256\n",
            "weighted avg       0.96      0.96      0.96       256\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.96      0.97      0.97       133\n",
            "           1       0.97      0.96      0.96       123\n",
            "\n",
            "    accuracy                           0.96       256\n",
            "   macro avg       0.96      0.96      0.96       256\n",
            "weighted avg       0.96      0.96      0.96       256\n",
            "\n",
            "acc: 96.0975498540856\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Comparsion**"
      ],
      "metadata": {
        "id": "73EPhoR8b-f8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "head=[\"ACCURACY\",\"PRECISION\",\"RECALL\",\"F1\"]\n",
        "plt.figure(figsize=(5,5))\n",
        "plt.plot(head,hmsc,label=\"Default features\")\n",
        "plt.plot(head,msc,label=\"Changed features\")\n",
        "plt.title(\"feature selection\")\n",
        "plt.xlabel(\"PERFORMANCE METRICS\")\n",
        "plt.ylabel(\"SCORE\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        },
        "id": "fWh1kvBhb9RO",
        "outputId": "1d3f28f6-c2b7-40ad-8f11-baf95888387a"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**PERFORMANCE INCREASE DESPITE DROPPING A FEATURE**"
      ],
      "metadata": {
        "id": "ws4pP-9ThKxV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**New Features for prediction**"
      ],
      "metadata": {
        "id": "b4u-KQEsaJWg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = data[\"target\"]\n",
        "X = data.drop(columns=['target','fbs'])\n",
        "cols=X.columns\n",
        "for col in cols:\n",
        "   X[col]=minmax_scale(X[col])\n"
      ],
      "metadata": {
        "id": "8nrf1qNBW3IS"
      },
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**HYPER TUNNING OF PARARMETER**\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "T3h5ZjV2Nq8I"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##XG Boost"
      ],
      "metadata": {
        "id": "J3EsnPQqtY2G"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "scaler = StandardScaler()\n",
        "X_train = scaler.fit_transform(X_train)\n",
        "X_test = scaler.transform(X_test)"
      ],
      "metadata": {
        "id": "B2FSpUBAoZpN"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**MAX DEPTH**"
      ],
      "metadata": {
        "id": "H30rjfAZpT8V"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "trs=[]\n",
        "tes=[]\n",
        "values = [i for i in range(2, 11)]\n",
        "\n",
        "\n",
        "for i in values:\n",
        "\n",
        "\tmodel= XGBClassifier(max_depth=i)\n",
        "\n",
        "\tmodel.fit(X_train, y_train)\n",
        "\n",
        "\ttrain_yhat = model.predict(X_train)\n",
        "\ttrain_acc = accuracy_score(y_train, train_yhat)\n",
        "\ttrs.append(train_acc)\n",
        "\n",
        "\ttest_yhat = model.predict(X_test)\n",
        "\ttest_acc = accuracy_score(y_test, test_yhat)\n",
        "\ttes.append(test_acc)\n",
        "\n",
        "\tprint('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))\n",
        "plt.ylabel(\"ACCURACY\")\n",
        "plt.xlabel(\"Max Depth-RF\")\n",
        "plt.plot(values, trs, '-o', label='Train')\n",
        "plt.plot(values, tes, '-o', label='Test')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 211
        },
        "id": "7tuoZ4_9oyd_",
        "outputId": "953e22f5-eacf-40d6-c219-17e5ae838904"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ">2, train: 0.937, test: 0.891\n",
            ">3, train: 0.986, test: 0.919\n",
            ">4, train: 1.000, test: 0.955\n",
            ">5, train: 1.000, test: 0.967\n",
            ">6, train: 1.000, test: 0.967\n",
            ">7, train: 1.000, test: 0.967\n",
            ">8, train: 1.000, test: 0.967\n",
            ">9, train: 1.000, test: 0.967\n",
            ">10, train: 1.000, test: 0.967\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**N-Estimators**"
      ],
      "metadata": {
        "id": "UvwfYFOFpxCH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "trs=[]\n",
        "tes=[]\n",
        "values = [i for i in range(50,1051,100)]\n",
        "\n",
        "\n",
        "for i in values:\n",
        "\n",
        "\tmodel= XGBClassifier(max_depth=3,n_estimators=i)\n",
        "\n",
        "\tmodel.fit(X_train, y_train)\n",
        "\n",
        "\ttrain_yhat = model.predict(X_train)\n",
        "\ttrain_acc = accuracy_score(y_train, train_yhat)\n",
        "\ttrs.append(train_acc)\n",
        "\n",
        "\ttest_yhat = model.predict(X_test)\n",
        "\ttest_acc = accuracy_score(y_test, test_yhat)\n",
        "\ttes.append(test_acc)\n",
        "\n",
        "\tprint('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))\n",
        "plt.ylabel(\"ACCURACY\")\n",
        "plt.xlabel(\"Max Depth-RF\")\n",
        "plt.plot(values, trs, '-o', label='Train')\n",
        "plt.plot(values, tes, '-o', label='Test')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 245
        },
        "id": "omiRPNG0pwhM",
        "outputId": "1a7afd04-0399-43ed-c217-de2d141a2474"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ">50, train: 0.961, test: 0.914\n",
            ">150, train: 0.995, test: 0.936\n",
            ">250, train: 1.000, test: 0.955\n",
            ">350, train: 1.000, test: 0.955\n",
            ">450, train: 1.000, test: 0.955\n",
            ">550, train: 1.000, test: 0.955\n",
            ">650, train: 1.000, test: 0.947\n",
            ">750, train: 1.000, test: 0.947\n",
            ">850, train: 1.000, test: 0.947\n",
            ">950, train: 1.000, test: 0.947\n",
            ">1050, train: 1.000, test: 0.947\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**LEARNING RATE**"
      ],
      "metadata": {
        "id": "OgcY8LiHqgfb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "trs=[]\n",
        "tes=[]\n",
        "values=[i for  i in np.arange(0.01,0.15,0.01)]\n",
        "\n",
        "\n",
        "for i in values:\n",
        "\n",
        "\tmodel= XGBClassifier(max_depth=3,n_estimators=350,learning_rate=i)\n",
        "\n",
        "\tmodel.fit(X_train, y_train)\n",
        "\n",
        "\ttrain_yhat = model.predict(X_train)\n",
        "\ttrain_acc = accuracy_score(y_train, train_yhat)\n",
        "\ttrs.append(train_acc)\n",
        "\n",
        "\ttest_yhat = model.predict(X_test)\n",
        "\ttest_acc = accuracy_score(y_test, test_yhat)\n",
        "\ttes.append(test_acc)\n",
        "\n",
        "\tprint('>%.2f, train: %.3f, test: %.3f' % (i, train_acc, test_acc))\n",
        "plt.ylabel(\"ACCURACY\")\n",
        "plt.xlabel(\"Learning Rate\")\n",
        "plt.plot(values, trs, '-o', label='Train')\n",
        "plt.plot(values, tes, '-o', label='Test')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 298
        },
        "id": "-VJWqvdYqjVO",
        "outputId": "fe4f817f-fe51-4005-a15c-6ea3181d8992"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ">0.01, train: 0.949, test: 0.894\n",
            ">0.02, train: 0.974, test: 0.905\n",
            ">0.03, train: 0.986, test: 0.919\n",
            ">0.04, train: 0.995, test: 0.936\n",
            ">0.05, train: 0.997, test: 0.944\n",
            ">0.06, train: 0.998, test: 0.950\n",
            ">0.07, train: 0.998, test: 0.950\n",
            ">0.08, train: 1.000, test: 0.955\n",
            ">0.09, train: 1.000, test: 0.955\n",
            ">0.10, train: 1.000, test: 0.955\n",
            ">0.11, train: 1.000, test: 0.955\n",
            ">0.12, train: 1.000, test: 0.955\n",
            ">0.13, train: 1.000, test: 0.955\n",
            ">0.14, train: 1.000, test: 0.947\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**MIN CHILD WEIGHT**"
      ],
      "metadata": {
        "id": "A8HuqUks2jzv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "trs=[]\n",
        "tes=[]\n",
        "values=[i for  i in np.arange(0,10,1)]\n",
        "\n",
        "\n",
        "for i in values:\n",
        "\n",
        "\tmodel= XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=i)\n",
        "\n",
        "\tmodel.fit(X_train, y_train)\n",
        "\n",
        "\ttrain_yhat = model.predict(X_train)\n",
        "\ttrain_acc = accuracy_score(y_train, train_yhat)\n",
        "\ttrs.append(train_acc)\n",
        "\n",
        "\ttest_yhat = model.predict(X_test)\n",
        "\ttest_acc = accuracy_score(y_test, test_yhat)\n",
        "\ttes.append(test_acc)\n",
        "\n",
        "\tprint('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))\n",
        "plt.ylabel(\"ACCURACY\")\n",
        "plt.xlabel(\"Min Child Weight\")\n",
        "plt.plot(values, trs, '-o', label='Train')\n",
        "plt.plot(values, tes, '-o', label='Test')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        },
        "id": "1tZ5JBjj2jXN",
        "outputId": "4b2543fa-fa66-40a9-8cfb-ae86a403770e"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ">0, train: 1.000, test: 0.955\n",
            ">1, train: 1.000, test: 0.955\n",
            ">2, train: 1.000, test: 0.955\n",
            ">3, train: 0.998, test: 0.942\n",
            ">4, train: 0.997, test: 0.936\n",
            ">5, train: 0.998, test: 0.950\n",
            ">6, train: 0.995, test: 0.939\n",
            ">7, train: 0.995, test: 0.942\n",
            ">8, train: 0.989, test: 0.936\n",
            ">9, train: 0.974, test: 0.922\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Col sample by tree**"
      ],
      "metadata": {
        "id": "BTMaYO8zCM9A"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "trs=[]\n",
        "tes=[]\n",
        "values=[i for  i in np.arange(0,1,0.1)]\n",
        "\n",
        "\n",
        "for i in values:\n",
        "\n",
        "\tmodel= XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=3,colsample_bytree=i)\n",
        "\n",
        "\tmodel.fit(X_train, y_train)\n",
        "\n",
        "\ttrain_yhat = model.predict(X_train)\n",
        "\ttrain_acc = accuracy_score(y_train, train_yhat)\n",
        "\ttrs.append(train_acc)\n",
        "\n",
        "\ttest_yhat = model.predict(X_test)\n",
        "\ttest_acc = accuracy_score(y_test, test_yhat)\n",
        "\ttes.append(test_acc)\n",
        "\n",
        "\tprint('>%.2f, train: %.3f, test: %.3f' % (i, train_acc, test_acc))\n",
        "plt.ylabel(\"ACCURACY\")\n",
        "plt.xlabel(\"col sample by tree\")\n",
        "plt.plot(values, trs, '-o', label='Train')\n",
        "plt.plot(values, tes, '-o', label='Test')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        },
        "id": "HMxy-4m0CYSn",
        "outputId": "75442706-138a-4aa6-b44f-d33c5408fd8d"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ">0.00, train: 0.959, test: 0.925\n",
            ">0.10, train: 0.959, test: 0.925\n",
            ">0.20, train: 0.995, test: 0.950\n",
            ">0.30, train: 0.997, test: 0.944\n",
            ">0.40, train: 0.998, test: 0.950\n",
            ">0.50, train: 0.998, test: 0.950\n",
            ">0.60, train: 0.998, test: 0.950\n",
            ">0.70, train: 0.998, test: 0.950\n",
            ">0.80, train: 0.998, test: 0.950\n",
            ">0.90, train: 0.998, test: 0.942\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Lambda**"
      ],
      "metadata": {
        "id": "aNyKkbS5DEIK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "trs=[]\n",
        "tes=[]\n",
        "values=[i for  i in np.arange(0,10,1)]\n",
        "\n",
        "\n",
        "for i in values:\n",
        "\n",
        "\tmodel= XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=3,colsample_bytree=0.2,reg_lambda=i)\n",
        "\n",
        "\tmodel.fit(X_train, y_train)\n",
        "\n",
        "\ttrain_yhat = model.predict(X_train)\n",
        "\ttrain_acc = accuracy_score(y_train, train_yhat)\n",
        "\ttrs.append(train_acc)\n",
        "\n",
        "\ttest_yhat = model.predict(X_test)\n",
        "\ttest_acc = accuracy_score(y_test, test_yhat)\n",
        "\ttes.append(test_acc)\n",
        "\n",
        "\tprint('>%.2f, train: %.3f, test: %.3f' % (i, train_acc, test_acc))\n",
        "plt.ylabel(\"ACCURACY\")\n",
        "plt.xlabel(\"col sample by tree\")\n",
        "plt.plot(values, trs, '-o', label='Train')\n",
        "plt.plot(values, tes, '-o', label='Test')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        },
        "id": "MKEwBgqpC7f7",
        "outputId": "86738eb8-29c3-4bf6-fed1-61e6997a5898"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            ">0.00, train: 0.995, test: 0.950\n",
            ">1.00, train: 0.995, test: 0.950\n",
            ">2.00, train: 0.992, test: 0.947\n",
            ">3.00, train: 0.989, test: 0.944\n",
            ">4.00, train: 0.985, test: 0.942\n",
            ">5.00, train: 0.985, test: 0.942\n",
            ">6.00, train: 0.982, test: 0.939\n",
            ">7.00, train: 0.979, test: 0.933\n",
            ">8.00, train: 0.982, test: 0.939\n",
            ">9.00, train: 0.979, test: 0.933\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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p08fpaysTNm0aZMyduxYRVEUZe7cucqKFSuM1x08eLBSXFxsEtumTZuUTp06KUeOHFGqqqqURx55RFm9erVSVFSkDBgwQKmoqFAURVEeeOABZc+ePZe9t65duxp/zs7OVkJDQ5UdO3YoiqIoP//8s/LKK68o1dXVisFgUMaOHats2bJF2b9/v/Lkk08aX3vatGnK8uXLr+n/RNgvqUGIBmXTpk3Exsbi7e0NgKenJwA7duxg4cKFANxzzz0kJCRc8XW6devGpEmTGDJkCIMGDQLUGUunT5/Onj170Gq1ZGVlGY8PCwszzvffpk0bevfuDUBISAibN282HjdkyBC0Wi1t27YlICDAOHfRBb/88gs//fQTH374IQDl5eUcO3bssnl8OnfuTEBAAADDhg1j+/btxMbGEhERwfr162nfvj2VlZWEhoZetcxatmxJ165dAdiwYQMbNmxgxIgRgFqjycrKYu/evezatcu43kNZWRnNmze/6msL+yYJQjRK06dP5/fff2f9+vXExcXxzTff8Omnn+Lj48PKlSuprq6mc+fOxuOdnJyMP2u1WuNzrVaLwWAw7tNoNCbXufQ5wNtvv0379u2vGJ+l17nvvvt47733aN++Pffee+81vVc3Nzfjz4qiMHbsWB588EGTYz755BNGjhzJCy+8cE2vKRoH6aQWDUpERARr1qyhsLAQgNOnTwNqjeDCko/fffcd4eHhV3ydI0eO0KVLF5577jm8vLzIy8vj3Llz+Pr6otVqWblypckH/7Vas2YN1dXVHDlyhOzsbNq1a2eyPzIykk8//RTl/BRolqbMTk9PJzs7m+rqalavXk337t0BdZK4vLw8Vq1axV133WX2XAcHByorK83ui4yM5JtvvqG4uBhQp7g/deoUvXr14ocffuDUqVOAWq65ubnX/f6FfZEahGhQgoODeeqppxg9ejRarZZbb72VN954g1dffZXJkyfzwQcfGDupr+TNN9/k8OHDKIpCREQEHTp04C9/+Qt///vfWbFiBX369DH55n2tWrRowahRoyguLua1117D2dnZZP/TTz/NrFmzuPvuu6murqZ169Zm7zoKCwtjxowZxk7qC81goDZjZWRk4OHhYTaG+++/n7vvvptbb72Vf/7znyb7IiMjOXDggLEG4ebmRkJCAkFBQfzjH//gscceo7q6GkdHR6ZOnUqrVq2uuwyE/ZDZXIWoJZMmTaJfv37ExsZa9TpPPvkkjzzyCL169bLqdYSQJiYhGoizZ88SExODs7OzJAdRJ6QGIYQQwiypQQghhDBLEoQQQgizJEEIIYQwSxKEEEIIsyRBCCGEMOv/Abjb4LlonzECAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**COMPARSION BETWEEN HYPERTUNED AND DEFAULT XG BOOSTING**"
      ],
      "metadata": {
        "id": "gSm2clW_rF_5"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**HOLD OUT**"
      ],
      "metadata": {
        "id": "Rm13TxwUZ3Gr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**DEFAULT**"
      ],
      "metadata": {
        "id": "TxIMmfysrF_6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)"
      ],
      "metadata": {
        "id": "ZiOX64aWUlu3"
      },
      "execution_count": 54,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fmodel=XGBClassifier()\n",
        "fmodel.fit(X_train,y_train)\n",
        "y_pred=fmodel.predict(X_test)"
      ],
      "metadata": {
        "id": "CEIZI1cKUlu3"
      },
      "execution_count": 55,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "msc=[]\n",
        "print(\"For default XG BOOST model:\")\n",
        "print(\"ACCURACY:\",accuracy_score(y_test,y_pred)*100)\n",
        "print(\"PRECISION:\",precision_score(y_test,y_pred)*100)\n",
        "print(\"RECALL:\",recall_score(y_test,y_pred,)*100)\n",
        "print(\"F1:\",f1_score(y_test,y_pred,)*100)\n",
        "msc.extend((accuracy_score(y_test,y_pred)*100,precision_score(y_test,y_pred)*100,recall_score(y_test,y_pred,)*100,f1_score(y_test,y_pred,)*100))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c2918df5-8cb0-45ad-be34-853c52db5e4a",
        "id": "5w4A7WF59CQ7"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For default XG BOOST model:\n",
            "ACCURACY: 91.92200557103064\n",
            "PRECISION: 92.26519337016575\n",
            "RECALL: 91.75824175824175\n",
            "F1: 92.01101928374656\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**HYPERTUNED**"
      ],
      "metadata": {
        "id": "HemoRBOvX4A6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =10)\n",
        "fmodel=XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=3,colsample_bytree=0.2,reg_lambda=4)\n",
        "fmodel.fit(X_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6cba24a9-b09b-4eaf-b8a7-bc55795e3f04",
        "id": "NhppbvhPUwuB"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "XGBClassifier(colsample_bytree=0.2, min_child_weight=3, n_estimators=350,\n",
              "              reg_lambda=4)"
            ]
          },
          "metadata": {},
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hmsc=[]\n",
        "y_pred=fmodel.predict(X_test)\n",
        "print(\"For hyper tuned XG BOOST model\")\n",
        "print(\"Testing dataset:\")\n",
        "print(\"ACCURACY:\",accuracy_score(y_test,y_pred)*100)\n",
        "print(\"PRECISION:\",precision_score(y_test,y_pred)*100)\n",
        "print(\"RECALL:\",recall_score(y_test,y_pred,)*100)\n",
        "print(\"F1:\",f1_score(y_test,y_pred,)*100)\n",
        "hmsc.extend((accuracy_score(y_test,y_pred)*100,precision_score(y_test,y_pred)*100,recall_score(y_test,y_pred,)*100,f1_score(y_test,y_pred,)*100))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "52675c7f-5a20-4577-93c0-2ab03505ed2f",
        "id": "tgEQ13BxUwuB"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For hyper tuned XG BOOST model\n",
            "Testing dataset:\n",
            "ACCURACY: 94.15041782729804\n",
            "PRECISION: 94.97206703910615\n",
            "RECALL: 93.4065934065934\n",
            "F1: 94.18282548476455\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Comparsion**"
      ],
      "metadata": {
        "id": "u8v72niXY3Du"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "head=[\"ACCURACY\",\"PRECISION\",\"RECALL\",\"F1\"]\n",
        "ind= np.arange(len(head))\n",
        "plt.figure(figsize=(8,8))\n",
        "plt.bar(ind-0.2,hmsc,0.4,label=\"Hypertuned\")\n",
        "plt.bar(ind+0.2,msc,0.4,label=\"Default\")\n",
        "plt.title(\"HYPERTUNING OF XG BOOST\")\n",
        "plt.xlabel(\"PERFORMANCE METRICS\")\n",
        "plt.xticks(ind,head)\n",
        "plt.ylabel(\"SCORE\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 513
        },
        "id": "Gldi-x30Y5mq",
        "outputId": "60a749d2-08fd-4839-9c73-8add291cfbc2"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 576x576 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAe4AAAHwCAYAAABgy4y9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3df3zO9f7H8ee1zTbOiNUMmQrN2SFMO2YhGbYxbMRJpxTpRMUISTSSza8okfz4qpPOkY6QX2NhFPkVJd3UklSysIkJG/v5+f7h7Dqu9sOvXeM9j/vttttt1+f6fN6f1+fz3nU99/ltsyzLEgAAMILL9S4AAABcPoIbAACDENwAABiE4AYAwCAENwAABiG4AQAwCMENAIBBCG6UG6Ghodq2bZvDsGXLlunhhx+WJA0fPlwvvviiw/uff/65goODlZaWppkzZ6phw4YKDAxUUFCQevXqpT179tjbCQgIUGBgoMNPamqqfd6NGzdWYGCgWrZsqZEjRyojI0Njxoyxj9uoUSN7+4GBgXryySe1c+dO3X///YWWpXfv3vrwww8lSTNnzlSDBg20Zs0a+/u5ublq0KCBUlJSJEkjR47U66+/LklKSUlRgwYN9I9//MOhzeHDh2vmzJn212fPntXEiRMVGhqqpk2b6oEHHlBMTIz27t1b7DrOzs7WtGnT9MADD6hx48YKCwvT/PnzdfHtIHr37q177rnHYT0VrMeLffvtt2rWrJkOHTpkH7Zv3z4FBQXZl0uSEhIS1LNnTzVt2lQhISHq2bOnFi5cqOJuQXHx/O+991498sgj2r9/v8M4mzZtUo8ePdS0aVMFBwdr2LBhOnbsmMM4x44d07BhwxQcHKymTZuqR48e2rRpk8M4GzZsUFRUlJo1a6bg4GA99thjOnz48CX7HbgmFlBOtG3b1tq6davDsKVLl1q9evWyLMuyTp48ad13333WZ599ZlmWZZ0/f94KCwuzli5dalmWZc2YMcMaNmyYZVmWlZ2dbU2ePNlq2bKllZ+f79DOpeadlpZmdenSxXrttdccxrm4/QI7duywWrduXai9Rx991Fq8eLF9uubNm1sRERFWbm6uZVmWlZOTY/n7+1uHDx+2LMuyXnjhBfv8Dh8+bPn7+1vNmze3vvjiC3ubw4YNs2bMmGFZlmVlZWVZ3bt3t/r06WPt37/fys3NtTIyMqy1a9faxylK//79rQcffNDav3+/lZOTY+3Zs8fq0KGDNX78+CJrv5Rp06ZZjz76qJWfn29lZ2dbXbp0sRYsWGB//+2337ZCQkKstWvXWmfOnLHy8/Otb775xho6dKiVlZVVZJsXzz83N9eaPn261bVrV/v7a9eutQIDA62VK1da586ds9LS0qyRI0dabdu2tU6dOmVZlmWlp6dbbdu2tUaOHGmlpaVZ586ds1atWmUFBgZaa9eutSzLsn7++WerWbNm1rZt26z8/HzrzJkzVmJiovXrr7861FNUvwPXgi1u3DSqVauml156SbGxscrMzNSbb74pPz8/de/evdC4FSpUULdu3XT8+HGlp6df0Xx8fHzUqlUrJScnl1bpatWqlSpUqKCVK1de9jT9+vWzb4X/0YoVK5SamqpZs2bJ399frq6uqlSpkiIiIjRo0KAip9m+fbu2bt2qmTNnyt/fX25ubmratKleffVVLVy40GHL+XINHDhQx48f13/+8x/NnTtXlSpV0qOPPipJOnPmjGbMmKGxY8cqIiJCXl5estls+stf/qJp06bJ3d39ku27uroqMjJSBw8elCRZlqXJkyfr6aefVpcuXeTp6SkfHx/Fx8erUqVKevfddyVJ7777ripVqqT4+Hj5+PjI09NTnTt31oABAzR58mRZlqXk5GTVrl1bISEhstls8vLyUnh4uGrVqnXF6wG4EgQ3biodO3ZUw4YNNXToUC1evFjjx48vcrzs7GwtW7ZMNWvWlLe39xXN49ixY9qyZYvq1KlTGiVLkmw2mwYPHqw333xTOTk5lzXN3//+d/3888+FDh9I0rZt29SqVStVqlTpsmvYunWrmjRpopo1azoMb9KkiWrUqKHt27dfdlsF3N3dFR8fr6lTp+qdd95RfHy8XFwufC3t2bNH2dnZateu3RW3WyA7O1urVq1SkyZNJEk//vijjhw5ooiICIfxXFxcFBYWZl9X27ZtU1hYmL2WAh07dtSRI0f0008/qWHDhvrxxx81YcIE7dixQxkZGVddJ3AlCG6UK88++6yCgoLsP+PGjSs0ztixY7Vz504988wzhUIoMTFRQUFBatOmjb755hu9+eab9vf27t3r0Hb79u0LzTswMFBt2rSRt7e3YmJiSnXZ2rVrJ29vb/ux70vx9PTUgAEDNH369ELv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rl27NGrUKK1evVpz5sxRixYtNHHiRJ0+fVo9e/bUfffdJ0n69ttvtXLlSlWtWlU7d+7UO++8o7lz50qSli1bVmx9mZmZatKkiZ577jlNmTJFixcv1jPPPKP4+Hg9/vjjCgoK0pEjR9SvXz+tXbtWs2bNUrNmzTRw4EB98sknWrJkSamsJ4IbAHBD8PT01IoVK+yvP/jgA33//feSpB49emj+/Pn2rebx48fbx4uMvLA1/9e//lVnz57V6dOn9dlnn2njxo165513JF14aMfRo0clSS1btlTVqlWvuL4KFSqobdu2kqRGjRpp69atkqRt27bphx9+sI939uxZZWRkaNeuXXrzzTclSQ888IBuueWWK55nUQhuAMAN795779W4ceO0c+dO5eXlyd/f3/7eH8/MLng9Y8YM1a1b1+G9vXv3lnhtuKurq/Lz8+2vs7Ky7L9XqFDB3raLi4vy8i4ct8/Pz9fixYvL7ElmnJwGADBCdHS0hg0bpu7duzsMX7NmjSRp9+7dqly5sipXrqxWrVrp3//+t/248rfffltkm3/605+UkZFhf3377bfru+++U35+vo4ePaqvv/76knW1atVK//rXv+yvC+729te//tV+xvqnn36q33///QqWtngENwDACF26dNHp06fVuXNnh+EeHh6Kjo7Wyy+/rPj4eEnSM888o9zcXHXt2lWRkZF64403imyzQYMGcnFxUdeuXfXuu+/q3nvv1e23365OnTopLi5ODRs2vGRdo0eP1r59+9SlSxd16tRJixYtkiQ9++yz2r17tyIjI7V+/XrVqlXrGtfABTartE5zc6Kb/ZmsN+uym4a+MgP9VLQ/rpfzOXnyrOBaau1fTXt/vOVpYmKikpKS9Oqrr9qH9e7dWyNGjNA999xTarWWtaL+Jkv6O+UYNwCgkNIM7dJob/z48dq8ebPmzZtXShWZi+AGANzwYmNjixx+8bHlmwXHuAEAMAjBjRvajXibxOLUubPupUcCgGvErnLc0Er7tovOdC23dASAy8UWNwAABrkpg5vdrwBuVjfy919AQICioqIUGRmprl27auH77zvcxaw4kydPVmRkpCZPnnxV8y14nGhZPuLzWtyUu8rZ/QrgZlXc99//da2pnJRT9tcBPu6q4FGp1Oabk5Wp5OPZJY5Twd1D42ctkCT9nn5Sb097RZkZGYqJiSlx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HRYWpoSEBL322muaPHmywsPD1bFjR3322Wf605/+pD//+c8aNWqUhg0bpo4dO6pz5872S4Tatm2roKAgPfjgg4qKitKXX36p559/vsh5t2/fXufOndO7776rFi1ayN3d3f5eu3bttGnTJmVnZys+Pl4nTpxQhw4d1LlzZ7344ovy9vZ23kox3F/+8hc1aNBAq1evllT4mOl7770nSZe1Xk+cOKGnn35anTt3VteuXeXq6qpHH33UYRybzaZZs2YpMTFRYWFhCg8Pl4eHh4YOHVpkfQMGDNDRo0edsORmutb+Ku4zXNDeTz/9pPvvv9/+s3btWknS2LFj7cMeeuihMlzim1doaKgmTZqkjz76SPfff79++OGH613SdcctTwEAMAhb3AAAGITgBgDAIAQ3AAAGIbgBADAIwQ0AgEFu7js6AFcoICBA/v7+ysvLU926dTV58mRVrFjRPrxAZGSknnrqKfXu3VtpaWny8PBQhQoVFBcXp4CAAEkXLnP505/+ZL8RztixY9WsWTMdOHBA48ePV2pqqizLUlRUlJ555hnZbDYtW7ZMU6ZMka+vr7KystSrVy/16dNHkjRz5ky9+eabWrdune644w5J0rvvvquJEydqyZIluueeeyRJycnJio6O1v/93//p/vvvt9fcoEED9e3bVyNHjpQkvf3228rMzNSgQYMkScuXL9f8+fNls9nk6uqqLl26qF+/fho5cqQ+//xzVa5cWdKF66w/+OADh/W2c+dOPfbYY4qLi1PPnj0d6hgxYkSx7fTs2dN+adfBgwd11113ycXFRa1bt1bdunVLXBeVKlVSv3797Mvy4YcfysPDQ25uburdu7eio6O1adMmvfHGG8rPz1dubq4ee+wx9erV61r/TACnIriBK3A5Txr7o6lTp+qee+7R0qVLNWXKFP3zn/+0v7dgwQKH68DPnz+vp59+Wi+//LJatWqlc+fOadCgQXr//ff1yCOPSLpwe84xY8YoPT1dERERCg8PV82aNSVJ/v7+SkhI0DPPPCPpwtPp7r77bod6Ln4i1sXB7e7urnXr1umpp54qdG36p59+qgULFujtt9+Wr6+vsrOz7TePkaQRI0YoIiKixHXn7++vtWvX2oN79erVhe4kWFQ7BQ9iCQ0NdVhfy5YtK3FdFFi0aJG2bdumJUuWyMvLS2fPntX69euVk5Oj2NhYLVmyRDVq1FB2drZSUlJKXAbgRsCucuAqFfekseJczhOtVq1apWbNmqlVq1aSLmx1jhkzRvPmzSs0brVq1XTHHXfo+PHj9mHt27e336P7l19+UeXKlR1un2tZlhITEzVp0iRt3bpVWVlZ9vfc3Nz00EMPacGCBYXmNW/ePI0YMUK+vr6SLoT83/72t8tedkmqVauWsrKy9Ntvv8myLG3ZssXhH4drUdS6KDB37ly9/PLL8vLyknThYS7dunVTRkaG8vLyVLVqVUkXlqlu3bqlUg/gTAQ3cBX++KSxi59sFBUVpTVr1hSaZsuWLYXu1vX4448rKirKvhX6ww8/FHpqWJ06dZSZmamzZ886DD9y5IiysrLUoEED+7CCJ4x9//33SkhIUKdOnRym+fLLL1W7dm3VqVNHwcHBhW7X+sgjj2jVqlU6c+aMw/BLPd1uypQp9mUfNmxYseOFh4crMTFRX375pRo2bOhw578raeePiloX0oX7v2dkZMjPz6/QNFWrVlVoaKjatm2roUOHauXKlcrPz7/seQLXC7vKgStQ3JPGStpVPnz4cOXk5CgzM7PQOH/cVX451qxZo127dumnn35SbGxsoWcVFzzp6rPPPtOCBQu0bNky+3sJCQmKjIy0j7dixQqFh4fb3/fy8rLfMtTT0/Oya7qcXeXShUeePvfcc/rxxx8VGRlpf4b8lbZT4FLr4lLi4+O1f/9+bd++Xe+88462bdumSZMmXVEbQFljixu4AgUBvWLFCsXGxhbaYizK1KlTlZSUpG7dumn8+PEljlu/fn198803DsMOHz6sSpUq2Xf1durUSatWrdKiRYs0bdq0QruH27Ztq5UrV6pWrVr2aaQLDzJZt26dZs2apdDQUMXFxWnLli2FtuQff/xxLV26VOfOnXOoqzSeV+3j4yM3Nzdt3br1qh5z+keXWhdeXl6qVKmS/bkARWnQoIH69Omjd955p9AT24AbEcENlAGbzabBgwfrq6++0sGDB4sdr0uXLvriiy+0bds2SRe28OPi4vTkk08WGveee+5R165d7WddF6hYsaKGDx+uAQMGOAzfvn27GjRooE8//VQbN27Upk2bFBYWpg0bNjiMV7VqVUVERGjJkiX2Yf3799err75qD8bs7Gx9+OGHV7YS/ismJkbPP//8JR+NeiWKWxeS9NRTT2ncuHH2f1AyMjK0fPlyZWRkaOfOnfbxvvvuO91+++2lVhPgLOwqB0rBxbvQJal169YaPny4wzienp564okn9Pbbb2vChAlFtuPp6am33npLcXFxGjdunPLz8xUVFVXo6WIF/vGPf6h79+7q37+/w/CC3eEXS0hIKPKJWIsWLVJ0dLTD8CeeeEILFy60v27Tpo1+++039e3bV5ZlyWaz2c/2li4cm549e7b99Ycffljs3ohmzZoVOfxK2/mj4tbF3//+d2VmZurBBx9UhQoV5ObmZl+O+fPna8yYMfL09FTFihU1ceLEy5oXcD3xdDAAAAzCrnIAAAxCcAMAYBCCGwAAgxDcAAAYhOAGAMAgBDcAAAYhuAEAMAjBDQCAQf4fZG3s1ZS8yEQAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**KFOLD**"
      ],
      "metadata": {
        "id": "tQlBBE0JYMdX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**DEFAULT-K FOLD**"
      ],
      "metadata": {
        "id": "1HozVQ8hYBnp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "acc2=[]\n",
        "dms=[]\n",
        "p1=[]\n",
        "r1=[]\n",
        "f1=[]\n",
        "\n",
        "\n",
        "kf=KFold(n_splits=3)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  xgb.fit(X_train,y_train)\n",
        "  y_pred = xgb.predict(X_test)\n",
        "  acc2.append(accuracy_score(y_test,y_pred))\n",
        "  p1.append(precision_score(y_test,y_pred))\n",
        "  r1.append(recall_score(y_test,y_pred))\n",
        "  f1.append(f1_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",sum(acc2)*100/len(acc2))\n",
        "dms.extend((sum(acc2)*100/len(acc2),sum(p1)*100/len(p1),sum(r1)*100/len(r1),sum(f1)*100/len(f1)))\n",
        "    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28d1ea4a-587d-44dd-ac67-01483ca75e8c",
        "id": "N2ErfIhrrF_7"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.97      0.96       158\n",
            "           1       0.97      0.96      0.96       184\n",
            "\n",
            "    accuracy                           0.96       342\n",
            "   macro avg       0.96      0.96      0.96       342\n",
            "weighted avg       0.96      0.96      0.96       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.96      0.91      0.93       170\n",
            "           1       0.91      0.96      0.93       172\n",
            "\n",
            "    accuracy                           0.93       342\n",
            "   macro avg       0.93      0.93      0.93       342\n",
            "weighted avg       0.93      0.93      0.93       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.93      0.93       171\n",
            "           1       0.93      0.92      0.93       170\n",
            "\n",
            "    accuracy                           0.93       341\n",
            "   macro avg       0.93      0.93      0.93       341\n",
            "weighted avg       0.93      0.93      0.93       341\n",
            "\n",
            "acc: 94.04743530380203\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**HYPERTUNED K-FOLD**"
      ],
      "metadata": {
        "id": "E6pkxAxtrF_5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "acc1=[]\n",
        "p1=[]\n",
        "r1=[]\n",
        "f1=[]\n",
        "hmsc=[]\n",
        "model=XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=3,colsample_bytree=0.2,reg_lambda=4)\n",
        "\n",
        "kf=KFold(n_splits=3,shuffle=True,random_state=10)\n",
        "\n",
        "for train_index, test_index in kf.split(X):\n",
        "  X_train, X_test = X.iloc[train_index], X.iloc[test_index]\n",
        "  y_train, y_test = y.iloc[train_index], y.iloc[test_index]\n",
        "\n",
        "  \n",
        "  model.fit(X_train,y_train)\n",
        "  y_pred = model.predict(X_test)\n",
        "\n",
        "  acc1.append(accuracy_score(y_test,y_pred))\n",
        "  p1.append(precision_score(y_test,y_pred))\n",
        "  r1.append(recall_score(y_test,y_pred))\n",
        "  f1.append(f1_score(y_test,y_pred))\n",
        "  print(classification_report(y_test,y_pred))\n",
        "print(\"acc:\",sum(acc1)*100/len(acc1))\n",
        "hmsc.extend((sum(acc1)*100/len(acc1),sum(p1)*100/len(p1),sum(r1)*100/len(r1),sum(f1)*100/len(f1)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "afb9951e-6e6a-4f92-83ab-d14338e3962b",
        "id": "_Min0KZFrF_6"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.93      0.95      0.94       167\n",
            "           1       0.95      0.93      0.94       175\n",
            "\n",
            "    accuracy                           0.94       342\n",
            "   macro avg       0.94      0.94      0.94       342\n",
            "weighted avg       0.94      0.94      0.94       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.94      0.94       171\n",
            "           1       0.94      0.95      0.94       171\n",
            "\n",
            "    accuracy                           0.94       342\n",
            "   macro avg       0.94      0.94      0.94       342\n",
            "weighted avg       0.94      0.94      0.94       342\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.96      0.95      0.96       161\n",
            "           1       0.96      0.97      0.96       180\n",
            "\n",
            "    accuracy                           0.96       341\n",
            "   macro avg       0.96      0.96      0.96       341\n",
            "weighted avg       0.96      0.96      0.96       341\n",
            "\n",
            "acc: 94.73284057324805\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "head=[\"ACCURACY\",\"PRECISION\",\"RECALL\",\"F1\"]\n",
        "ind= np.arange(len(head))\n",
        "plt.figure(figsize=(8,8))\n",
        "plt.bar(ind-0.2,hmsc,0.4,label=\"Hypertuned\")\n",
        "plt.bar(ind+0.2,dms,0.4,label=\"Default\")\n",
        "plt.title(\"HYPERTUNING OF XG BOOST\")\n",
        "plt.xlabel(\"PERFORMANCE METRICS\")\n",
        "plt.xticks(ind,head)\n",
        "plt.ylabel(\"SCORE\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 513
        },
        "outputId": "69c00abc-d1ef-4ccb-fe08-c14203e1a9c3",
        "id": "VOm3HboRrF_7"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 576x576 with 1 Axes>"
            ],
            "image/png": "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++2321/Hx8crICBADRo0UGhoaL7tJScny8fHJ9/3fHx8HPZMREdH29dT586dC6wzd4vf19dXNWrUcJhfuXLl5ObmZh/28MMPKyAgQHXr1tWOHTsu2Wbu/Bs0aKD//ve/6tu3r71NSSpfvnyBy3CpZc2dLjk5WVWrVtVHH32kxMREDRgwQI0bN7af2wA4E8GNYmX69OnauXOn/WfUqFF5xrn99ttVrlw53XPPPXneCwsL086dO7V161Z9+OGHqlOnjv29evXqObS9Zs2aPPPetWuXPvroIx0+fPiKdrG7uroqKysrz/DMzEyHwMo1YMAAvfvuu0pPT79s25LUrVs3/fHHH1q3bp3D8LJly+rEiRP2135+ftq5c2eBW/TlypVzmOZiJ06cULly5eyvX3nlFft6+uKLLwqscfz48WrUqJESExMVGxvrUGNycrLD+vnkk0+0c+dOlS1bVjk5OZdsM3f+e/fu1cyZMxUZGakffvjBXmNSUlKBy3CpZc2dLne8+vXr6+2339a2bds0b9487dixQ++++26Bywv8UwQ3UMgaNWqkLl26aMKECZcdt3LlykpOTnbYSrMsS0ePHs33WGmTJk1055136uOPP76iWtzd3dW3b1+9/fbbDmdhBwUFafPmzUpNTb2idiTp/vvv1549e3Ts2DGH4bnDGjdufMVt5dqyZYvWrVun0aNH69VXX1VMTIxOnz4tSfL395e7u7vWrl171e3mcnFxUUBAgKpVq6bNmzerevXqqlixouLi4hzGy8nJ0apVq+zLEBQUpNWrV+f5crBy5UpVqlRJd999d5555Z5lf/DgwWuuF7gSBDfgBE8++aS2bNmiH374ocDxKleurHr16mnSpElKSUlRRkaGZs+ebT/xKz8DBgzQ7Nmzr7iW8PBwpaen6+uvv7YPi4iIkI+Pj/r27asff/xR2dnZSk9P1759+y7Zzv3336+goCD169dPBw8eVHZ2tnbv3q0hQ4bokUce0V133XXFNUlSamqqoqKi9PLLL8vb21stWrTQ/fffr3HjxkmSypQpoxdeeEGjR49WXFyczp07p5ycHMXHxystLe2K57Nr1y4dOnRINWvWlM1m00svvaQZM2Zo2bJlSk9P14kTJzRixAidO3dOPXr0kCT16NFDZ8+e1YgRI3TixAmlp6dr+fLlevfddzV06FDZbDbt3LlTn332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KigxMbGoywAAwEg2y7KsopxhXFycNm3apJiYGEnS4sWLtXfvXo0cOfKS0+zevVseHh5FVSIAANdVenq66tevn+97bkVciypUqKDjx4/bXycmJqpChQoFTnOp4gEAuNkU+a7ye++9V7/88ouOHDmijIwMxcbGKjg4uKjLAADASEW+xe3m5qaRI0fq6aefVnZ2th588EHdc889RV0GAABGKvJj3AAA4Npx5zQAAAxCcAMAYBCC+x9Ys2aNatWqpUOHDtmH7d27V4899phCQ0MVERGhESNGKC0tTZK0YcMGdenSRe3atVNERITGjx8vSRo2bJji4uIc2vb395ckJSQkqG7dugoPD1e7du00dOhQZWZm2sfLyspS48aNNWnSJIfpU1JSNHLkSLVu3VpdunRR9+7d9c033ygsLEwHDhywjzd79uwCL8UrDvz8/BQeHq4OHTooMjLS3h8XD+/Tp4/OnDkjyXGd5/4sXrxYUv7rdc+ePZL+6rOcnBxFR0erQ4cO6tixox588EEdOXJEkhQcHKxTp05Jko4fP67nnntOISEhat26taKjo5WRkSFJ2r59u2rVqqV169bZl6N3797avn17EayxG1Nh95eU/2c4ISFBHTp0yDP//D6nKDy5/Zv7k5CQoOTkZHXv3l3+/v567bXXrneJN4wiPzmtOFm+fLkaNmyo2NhYRUZG6o8//lD//v315ptv2v+Jx8XFKSUlRUeOHNGYMWM0c+ZM1ahRQ9nZ2fr000+vaD7VqlXTkiVLlJ2drZ49e2rlypXq1KmTJGnz5s266667FBcXp0GDBslms0mSXnnlFVWpUkWrVq2Si4uLjhw5okOHDmn48OEaPXq05s2bp6SkJH3yySdauHChc1bQDcLT01NLliyRJA0aNEiffPKJevbs6TD8pZde0rx58/Tcc89J+mud/92l1uvFVqxYoaSkJC1dulQuLi46fvy4SpYs6TCOZVnq27evHnnkEc2YMUPZ2dmKiorSW2+9pZdeekmSVLFiRb377rtcdfE/zuivv3+Gcf1c3L+5UlNT1b9/fx08eFAHDx68TpXdeNjivkYpKSn69ttvFRMTo9jYWEnSvHnzFBERYQ9tSQoLC9Ptt9+u2bNnq0+fPqpRo4YkydXVVY8++uhVzdPV1VV169Z1uNNcbGysnnjiCVWqVEm7du2SJP3222/as2ePBgwYIBeXC11ctWpVPfDAA2revLl8fHy0ePFijR07Vn379tWtt976j9aFSQICAvTrr7/mGV6/fv3L3sGvoPV6sRMnTsjHx8c+TsWKFfOs423btsnDw0MPPvigpAt9O3z4cC1atMi+R+Bf//qXSpcurc2bN1/TshZnhdFf+X2GcWMpVaqUAgICuAHX3xDc12jt2rVq1qyZ7r77bpUrV0779u3TwYMHVbt27XzHP3jwoOrUqfOP5pmenq49e/aoWbNm9tdbtmxRcHCwOnToYP/nc/DgQfn5+cnV1TXfdoYPH6633npLp06dUkRExD+qySRZWVnauHGjfH19HYZnZ2dr69atDlu2v/32m8Nuu507d152veZq27at1q9fr/DwcI0fP1779+/PM05+fyteXl6qVKmSwxeLPn36aMaMGdeyuMVWYfVXfp9hXD/nz5+3998LL7xwvcu5obGr/BrlbulKUrt27f7RN/bc3duXkvtPKSEhQQ888ID+9a9/SZLWr1+vwMBAeXp6KiQkRO+8846GDx9+2flVqFBBjRs3zrOlWFzl/kOQLmxxd+3a1WF4YmKiatSooSZNmtinyW/X65U+DKdixYqKi4vT1q1btW3bNvXo0UNvv/22goKCrrr2++67T5K0c+fOq562uCns/srvM/xPv1zj2uW3qxz5I7ivwenTp7Vt2zb9+OOPstlsys7Ols1mU0REhL7//nu1bt06zzQ1a9bUvn377KF7sbJly9pPtMltv1y5cvbXuf+UTp06pUceeURr165Vq1atFBsbq2+//da+5ZFb1z333KMffvhB2dnZl9zacHFxse8+LO4u9Q8hd3haWpp69eqlefPm2f+R5+dK1msud3d3tWjRQi1atNDtt9+uNWvWOAR3zZo19eWXXzpMc+7cOR07dkx33nmn9u7dax+eu9Xt5nZzf1wLs78u9RkeOnSosxcD+Mdujv/chezLL79UeHi41q9fr3Xr1mnDhg2qUqWK7r//fi1evNjhrNVVq1bpjz/+UK9evTRz5kz9/PPPki6ceTx//nxJUqNGjbRixQr7GcVffPGFAgMD88zX29tbgwcP1qxZs3Tu3Dnt3LlTX331ldatW6d169Zp5MiRWr58uapVq6Y6depoypQpyr2/TkJCgr766isnrxkzlSxZUq+88oo++OADZWVlXXK8K12v33//vf34a05Ojg4cOKDKlSs7jBMUFKS0tDT72c/Z2dkaP368OnfunOdEtqZNm+rMmTMOVwPczAqjvy71GWbPBkxAcF+D5cuX59mqDgkJUWxsrN58801NmDBBoaGhatu2rb7++mvdcsst+te//qXhw4dr0KBBatu2rTp06GC/RKhly5YKCAjQgw8+qPDwcH333XcaMmRIvvNu3bq10tLSNGfOHDVu3Fju7u7291q1aqX169crIyNDMTExOnnypNq0aaMOHTro5Zdflre3t/NWiuH+/e9/q1atWlq+fLmkvMdMP/zwQ0m6ovV68uRJPffcc+rQoYM6deokV1dXPf744w7j2Gw2TZ8+XXFxcQoJCVFoaKg8PDw0cODAfOvr06ePjh075oQlN9M/7a9LfYZz2/v555/VvHlz+8/KlSslSaNGjbIPe+ihh4pwiW9ewcHBGj9+vL744gs1b95cP/300/Uu6brjlqcAABiELW4AAAxCcAMAYBCCGwAAgxDcAAAYhOAGAMAgN/cdHYCr5OfnJ19fX2VnZ6t69eqaMGGCSpYsaR+eq3379nr22WfVvXt3JSUlycPDQyVKlFB0dLT8/PwkXbjM5ZZbbrHfCGfUqFFq0KCBDh48qDFjxigxMVGWZSk8PFzPP/+8bDabFi1apIkTJ6pChQpKT0/Xww8/rB49ekiSpk6dqmnTpmnVqlW68847JUlz5szRuHHjtGDBAt17772SpPj4eEVEROj//u//1Lx5c3vNtWrVUs+ePTVs2DBJ0nvvvafU1FT169dPkrR48WLNnj1bNptNrq6u6tixo3r16qVhw4bpm2++UenSpSVduM76k08+cVhv27dv1xNPPKHo6Gh169bNoY6hQ4desp1u3brZL+06dOiQ7r77brm4uKhZs2aqXr16geuiVKlS6tWrl31ZPv/8c3l4eMjNzU3du3dXRESE1q9fr7fffls5OTnKysrSE088oYcffvif/pkATkVwA1fhSp409neTJk3Svffeq4ULF2rixIn64IMP7O/NnTvX4Trw8+fP67nnntOrr76qpk2bKi0tTf369dPHH3+sxx57TNKF23OOHDlSycnJCgsLU2hoqCpVqiRJ8vX1VWxsrJ5//nlJF55Od8899zjUc/ETsS4Obnd3d61atUrPPvtsnmvTN2zYoLlz5+q9995ThQoVlJGRYb95jCQNHTpUYWFhBa47X19frVy50h7cy5cvz3MnwfzayX0QS3BwsMP6WrRoUYHrItf8+fO1ZcsWLViwQF5eXjp37pxWr16tzMxMRUVFacGCBapYsaIyMjKUkJBQ4DIANwJ2lQPX6FJPGruUK3mi1bJly9SgQQM1bdpU0oWtzpEjR2rWrFl5xi1XrpzuvPNOnThxwj6sdevW9nt0//bbbypdurTD7XMty1JcXJzGjx+vzZs3Kz093f6em5ubHnroIc2dOzfPvGbNmqWhQ4eqQoUKki6E/H/+858rXnZJqly5stLT0/XHH3/Isixt2rTJ4YvDP5Hfusg1c+ZMvfrqq/Ly8pJ04WEunTt3VkpKirKzs1W2bFlJF5apevXqhVIP4EwEN3AN/v6ksYufbBQeHq4VK1bkmWbTpk157tb15JNPKjw83L4V+tNPP+V5ali1atWUmpqqc+fOOQw/evSo0tPTVatWLfuw3CeM/fjjj4qNjVW7du0cpvnuu+9UpUoVVatWTYGBgXlu1/rYY49p2bJlOnv2rMPwyz3dbuLEifZlHzRo0CXHCw0NVVxcnL777jvVrl3b4c5/V9PO3+W3LqQL939PSUlR1apV80xTtmxZBQcHq2XLlho4cKCWLl2qnJycK54ncL2wqxy4Cpd60lhBu8oHDx6szMxMpaam5hnn77vKr8SKFSu0Y8cO/fzzz4qKisrzrOLcJ119/fXXmjt3rhYtWmR/LzY2Vu3bt7ePt2TJEoWGhtrf9/Lyst8y1NPT84prupJd5dKFR56++OKLOnz4sNq3b29/hvzVtpPrcuvicmJiYnTgwAFt3bpV77//vrZs2aLx48dfVRtAUWOLG7gKuQG9ZMkSRUVF5dlizM+kSZO0du1ade7cWWPGjClw3Jo1a+r77793GHbkyBGVKlXKvqu3Xbt2WrZsmebPn6833ngjz+7hli1baunSpapcubJ9GunCg0xWrVql6dOnKzg4WNHR0dq0aVOeLfknn3xSCxcuVFpamkNdhfG8ah8fH7m5uWnz5s3X9JjTv7vcuvDy8lKpUqXszwXIT61atdSjRw+9//77eZ7YBtyICG6gCNhsNvXv31+7d+/WoUOHLjlex44d9e2332rLli2SLmzhR0dH6+mnn84z7r333qtOnTrZz7rOVbJkSQ0ePFh9+vRxGL5161bVqlVLGzZs0Lp167R+/XqFhIRozZo1DuOVLVtWYWFhWrBggX1Y79699frrr9uDMSMjQ59//vnVrYT/iYyM1JAhQy77aNSrcal1IUnPPvusRo8ebf+CkpKSosWLFyslJUXbt2+3j/fDDz/ojjvuKLSaAGdhVzlQCC7ehS5JzZo10+DBgx3G8fT01FNPPaX33ntPY8eOzbcdT09PvfPOO4qOjtbo0aOVk5Oj8PDwPE8Xy/XMM8+oS5cu6t27t8Pw3N3hF4uNjc33iVjz589XRESEw/CnnnpK8+bNs79u0aKF/vjjD/Xs2VOWZclms9nP9pYuHJueMWOG/fXnn39+yb0RDRo0yHf41bbzd5daF48++qhSU1P14IMPqkSJEnJzc7Mvx+zZszVy5Eh5enqqZMmSGjdu3BXNC7ieeDoYAAAGYVc5AAAGIbgBADAIwQ0AgEEIbgAADEJwAwBgEIIbAACDENwAABiE4AYAwCD/D68m6+05M+9UAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**CHECKING OVERFITTING**"
      ],
      "metadata": {
        "id": "NcuF-EU0T_iX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = data[\"target\"]\n",
        "new_x = data.drop(columns=['target','fbs'],axis=1)\n",
        "cols=new_x.columns\n",
        "for col in cols:\n",
        "   new_x[col]=minmax_scale(new_x[col])"
      ],
      "metadata": {
        "id": "cZzL3yq_hYWv"
      },
      "execution_count": 63,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=0.35, random_state =10)\n",
        "fmodel=XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=3,colsample_bytree=0.2,reg_lambda=4)\n",
        "fmodel.fit(X_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B2jAVCbki7Br",
        "outputId": "af2e4037-58c7-46b5-9630-a06380267230"
      },
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "XGBClassifier(colsample_bytree=0.2, min_child_weight=3, n_estimators=350,\n",
              "              reg_lambda=4)"
            ]
          },
          "metadata": {},
          "execution_count": 64
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred=fmodel.predict(X_test)\n",
        "print(\"For hyper tuned XG BOOST model\")\n",
        "print(\"Testing dataset:\")\n",
        "print(\"ACCURACY:\",accuracy_score(y_test,y_pred)*100)\n",
        "print(\"PRECISION:\",precision_score(y_test,y_pred)*100)\n",
        "print(\"RECALL:\",recall_score(y_test,y_pred,)*100)\n",
        "print(\"F1:\",f1_score(y_test,y_pred,)*100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ab542a90-32c2-4daa-fb41-36ca9a08b9f3",
        "id": "eSR44ZdHZJG9"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For hyper tuned XG BOOST model\n",
            "Testing dataset:\n",
            "ACCURACY: 94.15041782729804\n",
            "PRECISION: 94.97206703910615\n",
            "RECALL: 93.4065934065934\n",
            "F1: 94.18282548476455\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred=fmodel.predict(X_train)\n",
        "print(\"For hyper tuned XG BOOST model\")\n",
        "print(\"Training dataset:\")\n",
        "print(\"ACCURACY:\",accuracy_score(y_train,y_pred)*100)\n",
        "print(\"PRECISION:\",precision_score(y_train,y_pred)*100)\n",
        "print(\"RECALL:\",recall_score(y_train,y_pred,)*100)\n",
        "print(\"F1:\",f1_score(y_train,y_pred,)*100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f6lCi6LrgVMQ",
        "outputId": "34d57ffa-d1d7-4d82-8f79-65a5f1fd3d6b"
      },
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For hyper tuned XG BOOST model\n",
            "Training dataset:\n",
            "ACCURACY: 98.49849849849849\n",
            "PRECISION: 99.11764705882354\n",
            "RECALL: 97.96511627906976\n",
            "F1: 98.53801169590642\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**PREDICTION AND FINAL MODEL**"
      ],
      "metadata": {
        "id": "qhh_aCf2Ipaj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = data[\"target\"]\n",
        "X= data.drop(['target','fbs'],axis=1)\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state =8,)\n",
        "fmodel=XGBClassifier(max_depth=3,n_estimators=350,learning_rate=0.1,min_child_weight=3,colsample_bytree=0.2,reg_lambda=4)\n",
        "fmodel.fit(X_train,y_train)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EeBWmVGUjWMX",
        "outputId": "a7139e82-65ab-4852-e5ef-320ccf4aff9f"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "XGBClassifier(colsample_bytree=0.2, min_child_weight=3, n_estimators=350,\n",
              "              reg_lambda=4)"
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "> **Attribute Information**\n",
        "> * Age (age in years)\n",
        "> * Sex (1 = male; 0 = female)\n",
        "> * CP (chest pain type)\n",
        "> * TRESTBPS (resting blood pressure (in mm Hg on admission to the hospital))\n",
        "> * CHOL (serum cholestoral in mg/dl)\n",
        "> * RESTECH (resting electrocardiographic results)\n",
        "> * THALACH (maximum heart rate achieved)\n",
        "> * EXANG (exercise induced angina (1 = yes; 0 = no))\n",
        "> * OLDPEAK (ST depression induced by exercise relative to rest)\n",
        "> * SLOPE (the slope of the peak exercise ST segment)\n",
        "> * CA (number of major vessels (0-3) colored by flourosopy)\n",
        "> * THAL (defect-Reversible/Fixed/Normal)\n"
      ],
      "metadata": {
        "id": "ItyVOA_DJJeJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#input the value in order as shown above all can be input in form of interger values\n",
        "sample =[[52,1,0,125,212,1,168,0,1,2,2,3]]\n",
        "out1= pd.DataFrame(sample, columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])\n",
        "y_pred=fmodel.predict(out1)\n",
        "if(y_pred==1):\n",
        "  print(\"RISK OF HEART DISEASE\")\n",
        "else:\n",
        "  print(\"NO RISK OF HEART DISEASE\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lFS-Pl6rixGH",
        "outputId": "88e82c6f-6883-45ef-b563-fabde3534592"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NO RISK OF HEART DISEASE\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
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
      "version": "3.7.6"
    },
    "papermill": {
      "duration": 41.224233,
      "end_time": "2020-12-11T03:32:27.037873",
      "environment_variables": {},
      "exception": null,
      "input_path": "__notebook__.ipynb",
      "output_path": "__notebook__.ipynb",
      "parameters": {},
      "start_time": "2020-12-11T03:31:45.813640",
      "version": "2.1.0"
    },
    "colab": {
      "name": "AI_Milestone-4_Vaidyaa",
      "provenance": [],
      "collapsed_sections": [
        "T3h5ZjV2Nq8I"
      ]
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
