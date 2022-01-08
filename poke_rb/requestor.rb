# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'json'

def request_get(url)
  uri = URI(url)
  response = Net::HTTP.get_response(uri)
  JSON.parse(response.body) if response.is_a?(Net::HTTPSuccess)
end

def request_post(url, payload)
  uri = URI(url)
  port = uri.port == 443 ? nil : uri.port
  http = Net::HTTP.new(uri.host, port)
  request = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
  request.body = payload.to_json
  response = http.request(request)
  JSON.parse(response.body) if response.is_a?(Net::HTTPSuccess)
end
