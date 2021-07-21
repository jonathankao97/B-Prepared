import 'package:dio/dio.dart';
import 'package:fresh_dio/fresh_dio.dart';
import 'package:storage/storage.dart';
import 'models/models.dart';
import 'backend_token_storage.dart';

class BackendClient {
  BackendClient({
    required Storage storage,
    required String baseUrl,
    Dio? httpClient,
    Fresh<OAuth2Token>? fresh,
  }) {
    _fresh = fresh ??
        Fresh.oAuth2(
          tokenStorage: BackendTokenStorage(storage),
          refreshToken: _refreshToken,
        );
    _httpClient = (httpClient ?? Dio())
      ..options.baseUrl = baseUrl
      ..interceptors.add(_fresh);
  }

  late final Dio _httpClient;
  late final Fresh _fresh;

  static Future<BackendToken> _refreshToken(token, client) async {
    return BackendToken(
      accessToken: 'accessToken',
      refreshToken: 'refreshToken',
    );
  }

  Stream<AuthenticationStatus> get authenticationStatus =>
      _fresh.authenticationStatus;

  Future<void> authenticate({
    required String username,
    required String password,
  }) async {}

  Future<void> unauthenticate() async {}
}
