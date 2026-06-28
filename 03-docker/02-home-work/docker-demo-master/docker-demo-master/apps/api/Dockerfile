FROM node:20-bullseye

WORKDIR /opt/app

COPY package*.json ./
RUN npm install --legacy-peer-deps

COPY . .

ENV NODE_OPTIONS="--openssl-legacy-provider"

RUN npm run build converter

EXPOSE 3000
CMD ["node", "./dist/apps/converter/main.js"]
