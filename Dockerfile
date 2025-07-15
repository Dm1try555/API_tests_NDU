FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl unzip openjdk-17-jre-headless \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/workspace

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Встановлення Allure
ARG ALLURE_VERSION=2.21.0
RUN curl -Ls -o /tmp/allure.zip \
    "https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip" \
    && unzip /tmp/allure.zip -d /opt \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm /tmp/allure.zip

COPY . .

# Запуск тестів, генерація звіту та запуск сервера
CMD /bin/sh -c "\
    rm -rf allure-results allure-report && \
    pytest -sv --alluredir=allure-results && \
    allure generate allure-results --clean -o allure-report && \
    allure open -h 0.0.0.0 -p 8080 allure-report"
