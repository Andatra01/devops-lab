FROM node:14-alpine as build
WORKDIR /opt/app
COPY package*.json ./
RUN npm install
RUN npm install nestjs-rmq@2.0.4 --save-exact
COPY . .
RUN npm run build api

FROM node:14-alpine
WORKDIR /opt/app
COPY package*.json ./
RUN npm install --only=prod && npm install nestjs-rmq@2.0.4 --save-exact

COPY --from=build /opt/app/dist ./dist

CMD ["node", "./dist/apps/api/main.js"]