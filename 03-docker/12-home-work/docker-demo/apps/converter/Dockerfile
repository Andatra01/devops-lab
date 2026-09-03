FROM node:14-alpine as build-conv
WORKDIR /opt/app
ADD *.json ./
RUN npm install
RUN npm install nestjs-rmq@2.0.4 --save-exact
ADD . .
RUN npm run build converter

FROM node:14-alpine
WORKDIR /opt/app
ADD package.json ./
RUN npm install --only=prod && npm install nestjs-rmq@2.0.4 --save-exact
COPY --from=build-conv /opt/app/dist/apps/converter ./dist
CMD ["node", "./dist/main.js"]
